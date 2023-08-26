from distutils.core import setup
import py2exe

setup(
    windows=[{'script': 'eazy_translate.py'}],
    options={
        'py2exe': {
            'includes': ['Eazy Translate'],
            'icon_resources': [(1, 'icon.ico')]
        }
    },
    zipfile=None,
)
