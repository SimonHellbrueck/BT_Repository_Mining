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

Project | LC (t=100) | LM(t=20) | LPL(t=2) | TMM(t=5) | Total | Lifespan | Issues | LOC | Commits | Contributors | Stargazers
--- | --- | --- | --- |--- |--- |--- |--- |--- |--- |--- |---
java-design-patterns |36 |93 |97 |30 |256 |1569 |180 |64318 |2743 |196 |41682
RxJava |959 |3948 |1130 |670 |6707 |2147 |29 |343496 |6524 |324 |36456
elasticsearch |3589 |12329 |10577 |3068 |29563 |3212 |1829 |1490246 |73023 |1404 |36282
spring-boot |654 |539 |1119 |580 |2892 |2228 |389 |382812 |19876 |611 |31331
retrofit |56 |217 |139 |42 |454 |3002 |70 |25133 |1759 |154 |30429

