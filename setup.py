from setuptools import setup, find_packages


def requirements(path=''):
    try:
        with open(path, 'r') as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []


setup(
    name='ecmwf-pipeline',
    packages=find_packages(),
    author='Anthropocene Weather Group',
    author_email='anthropocene-weather-group@google.com',
    url='https://gitlab.com/google-pso/ais/grid_intelligence_ai/ecmwf',
    description='A GCP pipeline to make ECMWF data available to all of Alphabet.',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    platforms=['darwin', 'linux'],
    python_requires='>=3.5, <4',
    install_requires=requirements('requirements.txt'),
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    extras_require={
        'dev': requirements('dev_requirements.txt')
    },
    entry_points={
        'console_scripts': [
            'ecmwf_download=ecmwf_pipeline:cli',
        ]
    },
    project_urls={
        'Issue Tracking': 'https://bugdashboard.corp.google.com/app/tree;dashboardId=168372',
    },
)