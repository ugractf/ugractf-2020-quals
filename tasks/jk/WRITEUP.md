# Самый короткий анекдот: Write-up

Дан rar-архив. При попытке его распаковать (`rar x unrar.rar`) выясняется, что он повреждён:

```
Extracting  unrar                                                     40%
unrar                - checksum error
Total errors: 1
```

К счастью, в формат rar встроена возможность восстановления повреждённых архивов, если необходимая для восстановления информация была заложена в архив при его создании. Попробуем ей воспользоваться (`rar r unrar.rar`):

```
Building fixed.unrar.rar
Scanning... 100%
Data recovery record found
Repairing   0%
Corrupt 1018 bytes at 00000000 000017dc - data recovered 100%
1 blocks recovered.
Done
```

Появился файл _fixed.unrar.rar_, который распаковывается без ошибок и содержит, как и ожидалось, программу `unrar`.

Посчитаем разницу между «повреждённым» и исправленным архивом. Нужно применить к содержимому файлов операцию XOR: ненулевыми останутся только те байты, где случились изменения. По запросу [xor two files] находим [тред на Реддите](https://www.reddit.com/r/linuxquestions/comments/6kaqal/xor_of_two_files/), где указаны различные способы добиться нужного.

Результат операции XOR содержит окружённый нулевыми байтами флаг.

Флаг: **ugra_when_i_was_this_small_it_already_had_a_beard_that_long_d9b26c811561**

## Изначальный план

Изначально это задание было единым целым с заданием [Дед файл сделал](../gaffer/): после выполнения операции XOR должны были получаться те данные, которые в итоге стали условием отдельного задания, а не готовый флаг. Однако после недолгого обсуждения было решено расщепить задание на два.
