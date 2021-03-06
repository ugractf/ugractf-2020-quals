# Ugra CTF Quals 2020

23–24 мая 2020 года | [Сайт](https://2020.ugractf.ru) | [Результаты](SCOREBOARD.md)

## Таски

[Гимн года I](tasks/anthem1/) (stegano 50, kalan)  
[Гимн года II](tasks/anthem2/) (stegano 300, kalan)  
[Больше, чем RSA](tasks/bestrsa/) (crypto 250, nsychev)  
[Без единиц](tasks/devzero/) (stegano 250, kalan)  
[ЕГЭ](tasks/ege/) (ppc 350, vanya)  
[Экзамен по истории](tasks/exam/) (reverse 100, kalan)  
[Отзыв](tasks/feedback/) (crypto 50, nsychev)  
[Турбоптица](tasks/flappy/) (joy 150, abbradar)  
[Формулы](tasks/formulae/) (reverse 150, kalan)  
[Друзья](tasks/friends/) (web 250, nsychev)  
[Дед файл сделал](tasks/gaffer/) (crypto 100, kalan)  
[Хай-тек I](tasks/hitech1/) (forensics 100, nsychev)  
[Хай-тек II](tasks/hitech2/) (recon 150, nsychev)  
[Хай-тек III](tasks/hitech3/) (recon 300, nsychev)  
[Домашняя страница](tasks/homepage/) (web 50, nsychev)  
[Домофон](tasks/intercom/) (recon 100, vanya)  
[Кто](tasks/iswho/) (web 100, vanya)  
[Праздник в Японии](tasks/japclock/) (recon 200, kalan)  
[Самый короткий анекдот](tasks/jk/) (stegano 300, kalan)  
[Melodrama I](tasks/melodrama1/) (pwn 150, nsychev)  
[Melodrama II](tasks/melodrama2/) (pwn 250, nsychev)  
[Сапёр-неудачник](tasks/mines/) (reverse 200, abbradar)  
[Мнистерство статистики](tasks/mnist/) (ppc 350, kalan)  
[Мой Кирпич](tasks/mybrick/) (web 200, nsychev)  
[noteasy₅](tasks/noteasy5/) (crypto 150, kalan)  
[Менеджер паролей](tasks/passman/) (web 300, nsychev)  
[Самый важный таск](tasks/promotion/) (joy 25, nsychev)  
[Великий математик](tasks/pycfail/) (reverse 150, nsychev)  
[Святая простота](tasks/sancta/) (stegano 150, kalan)  
[IBM Selectric](tasks/selectric/) (crypto 200, kalan)  
[Расширение сознания](tasks/shrink/) (reverse 350, vanya)  
[Запросы](tasks/subdomain/) (forensics 300, nsychev)

### За кадром

[На лечение](tasks/therapy/) (ppc 150, nsychev)  
[Удалённая база данных](postmortem/UPDATE.md) (forensics 1337, nsychev)

## Команда соревнования

[Никита Сычев](https://github.com/nsychev) — руководитель команды разработки, разработчик тасков  
[Ваня Клименко](https://github.com/vanyaklimenko) — разработчик тасков и сайта  
[Калан Абе](https://github.com/kalan) — разработчик тасков и платформы  
[Коля Амиантов](https://github.com/abbradar) — разработчик тасков и платформы  
[Катя Ковальчук](https://www.behance.net/nclbrt) — иллюстратор

## Организаторы

Соревнования проводят команда [team Team], Депинформтехнологий Югры и ЮНИИИТ.

## Генерация заданий

Некоторые таски создаются динамически — у каждой команды своя, уникальная версия задания. В таких заданиях вам необходимо запустить генератор — обычно он находится в файле `generate.py` в директории задания. Обычно генератор принимает три аргумента — уникальный идентификатор, директорию для сохранения файлов для участника и названия генерируемых тасков (последний, как правило, не используется). Например, генератор можно запустить так:

```bash
./tasks/pycfail/generate.py 1337 /tmp/pycfail
```

Генератор выведет на стандартный поток вывода JSON-объект, содержащий флаг к заданию и информацию для участника, а в директории `/tmp/pycfail` появятся вложения, если они есть.

## Лицензия

Материалы соревнования можно использовать для тренировок, сборов и других личных целей, но запрещено использовать на своих соревнованиях. Подробнее — [в лицензии](LICENSE).
