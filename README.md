### Overview
* All scripts and the Python program can be executed at once by using the run_repository_analysis script: ```bash run_repository_analysis```
* The current versions of [PMD](https://github.com/pmd) and [Detekt](https://github.com/arturbosch/detekt) are used to analyse the repositories.
* By giving an argument to the Python program ```load_repository_names.py``` the size of the sample can be customized. However, ```load_repository_nams.py``` should be executed carefully since no exception handling for sending too many requests to GitHub has been implemented so far. The fetched repositories are then sorted by stars (in descending order).
```
python3 load_repository_names.py 100
python3 load_repository_names.py 200
python3 load_repository_names.py 300
python3 load_repository_names.py 400
python3 load_repository_names.py 500
python3 load_repository_names.py 1000
```

* When no argument is given the default value (n=5) will be used.

#### Example Output

* After executing all the scripts, CSV files will be created containing an output like the following (in this case for Java projects).
* t represents the threshold for the respective smell.

Project | LC (t=100) | LM(t=20) | LPL(t=3) | TMM(t=5) | Total | Lifespan | Issues | LOC | Commits | Contributors | Stargazers
--- | --- | --- | --- |--- |--- |--- |--- |--- |--- |--- |---
java-design-patterns | 0 | 56 | 65 | 0 | 121 | 1568 | 180 | 45044 | 2741 | 195 | 41658
RxJava | 161 | 2560 | 1130 | 167 | 4018 | 2146 | 29 | 343496 | 6524 | 324 | 36443
elasticsearch | 577 | 11543 | 10585 | 462 | 23167 | 3211 | 1824 | 1561731 | 73016 | 1404 | 36263
spring-boot | 55 | 451 | 1119 | 75 | 1700 | 2227 | 389 | 382812 | 19876 | 611 | 31319
retrofit | 9 | 161 | 139 | 5 | 314 | 3001 | 73 | 25133 | 1757 | 153 | 30420

