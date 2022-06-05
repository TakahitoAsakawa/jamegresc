import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jaresc", # 名前
    version="0.0.2", # バージョン設定
    author="takahito asakawa", # 名前
    author_email="s2022051@gmail.com", # メ-ルアドレス
    description='A package for visualization of Resource recovery amount and gain on sale data in Meguro', # 説明文書書き換え
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TakahitoAsakawa/jaresc", # GitHubURL
    project_urls={
        "Bug Tracker": "https://github.com/TakahitoAsakawa/jaresc", #GitHubURL
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    py_modules=['jaresc'], # 設定するモジュール名
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    entry_points = {
        'console_scripts': [
            'jaresc = jaresc:main' # src
        ]
    },
)