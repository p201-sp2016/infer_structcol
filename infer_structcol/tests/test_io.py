import os
import shutil
import numpy as np
import infer_structcol
from infer_structcol.io import convert_data,load_spectrum
from numpy.testing import assert_almost_equal

def test_io():
    # convert the spectrum
    filepath = os.path.dirname(os.path.abspath(__file__))
    direc = os.path.join(filepath, 'test_data')
    convert_data(np.array([450,600,800]), 'ref.txt', 'dark.txt', directory = os.path.join(direc, 'reflection'))
    
    # load the spectrum, creating a spectrum object
    convert_direc = os.path.join(direc,'reflection','converted','0_data_file.txt')
    spectrum = load_spectrum(refl_filepath = convert_direc)
    
    # check if equal to previously converted data
    assert_almost_equal(spectrum.wavelength[0],450)
    assert_almost_equal(spectrum.reflectance[0],0.35540140170390377)
    assert_almost_equal(spectrum.sigma_r[0],0.019663046306703093)
    
    spectrum.save(convert_direc)

    try:
        shutil.rmtree(os.path.join(direc, 'reflection', 'converted'))
    except:
        pass
