from infer_structcol.inference import find_max_like, run_mcmc
from infer_structcol.main import Sample, Spectrum
from infer_structcol.model import calc_model_spect

from numpy.testing import assert_equal

def test_calc_max_like():
    sample = Sample([450, 500, 550], particle_radius=119, thickness=120, particle_index=1.59, matrix_index=1)
    theta = (0.55, 0, 0) #these are the default starting values for lmfit calculation
    spect = calc_model_spect(sample, theta, seed=2)
    max_like_vals = find_max_like(spect, sample, seed=2)
    assert_equal(max_like_vals, (0.55000000014887396,0.0,0.0))

def test_run_mcmc():
    spectrum = Spectrum(500, reflectance = 0.5, sigma_r = 0.1)
    sample = Sample(500, 200, 200, 1.5, 1)
    theta = (0.5, 0, 0)
    run_mcmc(spectrum, sample, nwalkers=6, nsteps=1, theta=theta, seed=2)

