"""Power calculations for the G4 validity study (2026-10-18).

Sanity checks (defined before running):
  C1: paired t-test, d_z = 0.5, alpha=.05 two-sided, power=.80 -> n should be ~34 (G*Power reference value).
  C2: Pearson r = 0.30, alpha=.05 two-sided, power=.80 -> n should be ~84 (textbook value).
  C3: simulated repeated-measures correlation power should increase with trials per participant.
Outputs printed to stdout; redirect to power_results.txt.
"""
import numpy as np
from scipy import stats

rng = np.random.default_rng(20261018)
ALPHA, POWER = 0.05, 0.80


def paired_t_n(dz, alpha=ALPHA, power=POWER):
    for n in range(4, 2000):
        df = n - 1
        tcrit = stats.t.ppf(1 - alpha / 2, df)
        nc = dz * np.sqrt(n)
        pw = 1 - stats.nct.cdf(tcrit, df, nc) + stats.nct.cdf(-tcrit, df, nc)
        if pw >= power:
            return n, pw
    return None, None


def paired_t_power(dz, n, alpha=ALPHA):
    df = n - 1
    tcrit = stats.t.ppf(1 - alpha / 2, df)
    nc = dz * np.sqrt(n)
    return 1 - stats.nct.cdf(tcrit, df, nc) + stats.nct.cdf(-tcrit, df, nc)


def corr_n(r, alpha=ALPHA, power=POWER):
    z = np.arctanh(r)
    za, zb = stats.norm.ppf(1 - alpha / 2), stats.norm.ppf(power)
    return int(np.ceil(((za + zb) / z) ** 2 + 3))


def corr_power(r, n, alpha=ALPHA):
    z = np.arctanh(r) * np.sqrt(n - 3)
    za = stats.norm.ppf(1 - alpha / 2)
    return 1 - stats.norm.cdf(za - z) + stats.norm.cdf(-za - z)


def sim_rmcorr_power(n_part, n_trials, r_within, between_sd=1.0, n_sim=2000):
    """Within-participant association between an objective trial metric x and a
    per-trial subjective rating y; participants differ in rating offset (between_sd).
    Test = repeated-measures correlation (participant-centred Pearson, df = N(k-1)-1)."""
    hits = 0
    for _ in range(n_sim):
        x = rng.normal(size=(n_part, n_trials))
        offs = rng.normal(scale=between_sd, size=(n_part, 1))
        e = rng.normal(size=(n_part, n_trials))
        y = offs + r_within * x + np.sqrt(1 - r_within ** 2) * e
        xc = x - x.mean(axis=1, keepdims=True)
        yc = y - y.mean(axis=1, keepdims=True)
        r = (xc * yc).sum() / np.sqrt((xc ** 2).sum() * (yc ** 2).sum())
        df = n_part * (n_trials - 1) - 1
        t = r * np.sqrt(df / (1 - r ** 2))
        p = 2 * (1 - stats.t.cdf(abs(t), df))
        hits += p < ALPHA
    return hits / n_sim


print("== Paired t-test (within-subject condition contrast) ==")
for dz in [0.3, 0.5, 0.8, 1.0]:
    n, pw = paired_t_n(dz)
    print(f"d_z={dz:.1f}: n needed={n} (power={pw:.3f})")
for n in [18, 24, 39]:
    print(f"n={n}: power at d_z=0.5 -> {paired_t_power(0.5, n):.3f}; at d_z=0.8 -> {paired_t_power(0.8, n):.3f}")
print("minimum detectable d_z (80% power):")
for n in [18, 24, 39]:
    lo, hi = 0.05, 3.0
    for _ in range(60):
        mid = (lo + hi) / 2
        if paired_t_power(mid, n) >= POWER:
            hi = mid
        else:
            lo = mid
    print(f"  n={n}: d_z >= {hi:.2f}")

print("\n== Between-participant Pearson correlation (one value per participant) ==")
for r in [0.12, 0.3, 0.5]:
    print(f"r={r:.2f}: n needed={corr_n(r)}")
for n in [18, 24, 39]:
    print(f"n={n}: power r=0.3 -> {corr_power(0.3, n):.3f}; r=0.5 -> {corr_power(0.5, n):.3f}")

print("\n== Simulated repeated-measures correlation (trial-level objective metric vs per-trial rating) ==")
for n_part in [18, 24, 39]:
    for k in [4, 8, 16]:
        for rw in [0.2, 0.3]:
            pw = sim_rmcorr_power(n_part, k, rw)
            print(f"N={n_part}, trials/participant={k}, within-r={rw}: power={pw:.3f}")
