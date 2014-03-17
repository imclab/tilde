
# Tilde project: abstract class of a generic parser
# v060314

import os
import sys
import re
import time
from hashlib import sha224

from numpy import array


class Output:
    def __init__(self, filename=None):
        # (I)
        # inner Tilde objects
        self.starttime = time.time()
        self._coupler_ = False  # special attribute for an output which should be merged with another one by coinciding E_tot
        self.data = ''          # file contents holder; may be empty for some parsers!
        self._checksum = None   # 56-symbol hash NB: do not call directly
        
        # dict with calculation conditions, goes to *info*
        self.method = {
            'H':            None,
            'tol':          None,
            'k':            None,
            'spin':         None,
            'lockstate':    None,
            'technique':    {},
            'perturbation': None
            }

        # (II)
        # Tilde ORM objects
        # mapped onto database
        self.energy = None # in eV
        
        self.structures = [] # list of ASE objects with additional "hanged on" properties (e.g. periodicity: determination is a responsibility of a parser)

        self.symops = ['+x,+y,+z'] # legacy value

        self.electrons = {
            'basis_set':       {'bs': {}, 'ps': {}}, # valence and core electrons
            'eigvals':         {}, # raw eigenvalues {k:{alpha:[], beta:[]},}
            'projected':       [], # raw eigenvalues [..., ...] for total DOS smearing
            'dos':             {}, # in advance pre-computed DOS
            'bands':           {}  # in advance pre-computed band structure
        }
        # NB own properties for VASP: dos
        # NB own properties for CRYSTAL: impacts, proj_eigv_impacts, e_proj_eigvals

        self.phonons = {
            'modes':            {},
            'irreps':           {},
            'ir_active':        {},
            'raman_active':     {},
            'ph_eigvecs':       {},
            'ph_k_degeneracy':  {},
            'dfp_disps':        [],
            'dfp_magnitude':    None,
            'dielectric_tensor':False,
            'zpe':              None,
            'td':               None
            }

        # Tilde classification and technical info object
        # API call *classify* extends it with the new items
        self.info = {
            'warns':      [],
            'prog':       'unknown',
            'perf':       None,
            'location':   filename,
            'finished':   0,  # -1 for not, 0 for n/a, +1 for yes
            'duration':   None,
            'input':      None,
            
            'standard':   '',
            'formula':    '',
            'dims':       False,
            'elements':   [], # corresponds to sharp-signed multiple tag container in Tilde hierarchy : todo simplify
            'contents':   [],
            'lack':       False,
            'expanded':   False,
            'properties': {},
            'tags':       [], # corresponds to sharp-signed multiple tag container in Tilde hierarchy : todo simplify
            'calctypes':  [], # corresponds to sharp-signed multiple tag container in Tilde hierarchy : todo simplify
            'techs':      []  # corresponds to sharp-signed multiple tag container in Tilde hierarchy : todo simplify
            }

        # Tilde modules output object
        self.apps = {}

        # (III)
        # Tilde objects not (yet)
        # or not fully mapped onto database
        self.forces = array([])
        self.charges = None
        self.convergence = []
        self.ncycles = []
        self.tresholds = []
        self.comment = None

        # (IV)
        # settings objects
        
        # this is the limiting distance, after which the direction is considered non-periodic
        # be careful, as this has no physical meaning and may vary in different codes
        # e.g.: non-periodic component(s) are assigned 500 in CRYSTAL
        # hovewer, in PW codes this is ambiguous
        self.PERIODIC_LIMIT = 50

    def __getitem__(self, key):
        ''' get either by dict key or by attribute '''
        return getattr(self, key)
        
    def __setitem__(self, key, value):
        ''' in-place modifying '''
        return setattr(self, key, value)

    def __str__(self):
        ''' debug dumping '''
        out = ''
        for repr in dir(self):
            if not hasattr(getattr(self, repr), '__call__') and repr != '__doc__':
                if repr == 'structures' and len(getattr(self, repr)):
                    if len(getattr(self, repr)) > 1:
                        out += repr + " ->\nINITIAL:\n" + str( getattr(self, repr)[0] ) + "\nFINAL:\n" + str( getattr(self, repr)[-1] ) + "\n\n"
                    else:
                        out += repr + " -> " + str( getattr(self, repr)[-1] ) + "\n\n"
                else:
                    str_repr = str( getattr(self, repr) )
                    if len(str_repr) < 2000: out += repr + ' -> ' + str_repr + "\n\n"
                    else: out += repr + ' -> ' + str_repr[:1000] + '...\n\n'
        return out

    def warning(self, msg):
        ''' store diagnostic messages '''
        self.info['warns'].append(msg)

    def get_checksum(self):
        ''' retrieve unique hash '''
        if not self._checksum:
            file_sha224_checksum = sha224()
            file_sha224_checksum.update(str(self.structures) + str(self.energy)) # this is how unique identity is determined now
            return file_sha224_checksum.hexdigest()
        else:
            return self._checksum

    def benchmark(self):
        ''' benchmarking '''
        self.info['perf'] = "%1.2f" % (time.time() - self.starttime)
