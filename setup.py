from setuptools import setup, Extension

setup(name='seqmml',
      version='0.1',
      description='Hyperparameter Optimization based on Sequential Meta Machine Learning.',
      author='Zebin Yang and Aijun Zhang',
      author_email='yangzb2010@hku.hk, ajzhang@hku.hk',
      license='GPL',
      packages=['seqmml','seqmml.pybayopt','seqmml.pysequd', 'seqmml.pybatdoe'],
      install_requires=['joblib', 'numpy', 'pandas', 'scikit-learn', 'tqdm', 'hyperopt','smac', 'pyDOE', 'sobol_seq',
                   'pyunidoe @ git+https://github.com/ZebinYang/pyunidoe.git',
                   'spearmint @ git+https://github.com/ZebinYang/spearmint-lite.git'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'License :: OSI Approved :: BSD License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          ],
      zip_safe=False)
