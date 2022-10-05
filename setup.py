from setuptools import setup, find_namespace_packages


setup(
    name='clean_folder',
    version='1',
    description='Sorts folder',
    url='https://github.com/Andrew-157/home_work_6/blob/main/sort.py',
    author='Andrew-157',
    author_email='subotinandrew5@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': [
        'clean-folder = clean_folder.clean:main']}
)
