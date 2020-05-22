# Melodrama II: Write-up

Перед нами вторая часть задания «Мелодрама». Тот же самый порт и та же программа.

В этой части нас просят достать подпись главного редактора. Из кода видим, что эта подпись находится в файле `flag2.txt`. Редактор подписывает статьи, которые ему присылают — для этого есть специальная функция в интерфейсе:

```c
void sign_article() {
    <...>

    puts("Sending to chief editor, wait...");
    usleep(2000);
    
    strcpy(articles[id]->signature, signature);
    puts("Article is approved! Thank you!");
}
```

Наличие подписи в статье влияет лишь на то, что больше мы не можем применять к ней правки с добавлением контента. Однако, саму подпись мы не видим — интерфейса для её получения нет.

Обратим внимание на то, что подпись идёт сразу после нашего текста. Строки в языке Си ничего не знают о своей длине — они заканчиваются там, где находится нулевой байт. Таким образом, если мы каким-то образом сможем убрать нулевой байт из строки, то при чтении статьи выведется и подпись.

Такой способ находится при помощи системы редактирования — в имеющиеся статьи мы можем предлагать какие-то правки и применять их. Правки бывают двух типов: добавить кусок в статью и удалить кусок из статьи. Наше внимание должна привлечь весьма странная реализация чтения правки в функции `add_edit_insert`:

```c
    puts("Enter your change:");
    char content[141];
    int read = 0;
    while (1) {
        if (read == 141) {
            puts("Too long string.");
            return;
        }
        char next = getchar();
        content[read] = next;
        read += 1;

        if (next == '\n') {
            content[read - 1] = 0;
            break;
        }
    }

    // find first available slot
    for (int i = 0; i < EDITS; i++) {
        if (!edits[i]) {
            edits[i] = malloc(sizeof(edit_t));
            edits[i]->article = id;
            edits[i]->type = INSERT;
            edits[i]->offset = offset;
            edits[i]->count = read;
            edits[i]->content = malloc(141);
            strcpy(edits[i]->content, content);
            printf("Edit ID = %d\n", i);
            return;
        }
    }
```

Вместо чтения строки ввод читается посимвольно, чтение производится до символа переноса строки или до 140-го символа. После чего правка сохраняется.

В применении правки нас больше всего интересует вот эти строка:

```c
        int len = strlen(edits[id]->content);
        if (len + articles[article]->length > 140) {
            puts("Too long.");
            return;
        }

        <...>

        articles[article]->length += edits[id]->count;
```

Заметим, что здесь вперемешку используется `edits[id]->count` и `strlen(edits[id]->content)`. Самым же важным является то, что эти два значения попросту не равны между собой — при внимательном чтении кода становится заметно, что в переменной `read` учитывается и символ переноса строки, который впоследствии заменяется на нульбайт. Следовательно, при добавлении фрагмента в статью `articles[article]->length` становится на единицу больше фактической длины статьи.

Как же этим воспользоваться? Дело в том, что поле `length` используется и при удалении заметки: если мы добьёмся того, что это значение будет равно 141, у нас получится удалить 141-й символ — тот самый нульбайт.

Удаление произодится очень просто — кусок текста правее удаляемого фрагмента сдвигается влево так, чтобы «закрыть» удалённый фрагмент. Но в нашем случае если мы удалим нульбайт, то мы заменим его следующим символом — а именно, первым символом подписи. Вывод статьи приведёт к тому, что выведется как сам её текст, так и подпись (с продублированной первой буквой).

Итоговый алгоритм таков:

1. Заводим собственную заметку.
2. Дополняем её правкой до 140 символов: в поле `length` будет 141.
3. Подписываем статью, чтобы в поле подписи были нужные нам ненулевые байты.
4. Удаляем 141-й символ (то есть один символ с позиции 140 из-за индексации с нуля).
5. Выводим статью.

Поскольку вручную за 30 секунд (сервер даёт ровно такой интервал времени на сессию) это сделать сложно, можно [автоматизировать процесс](exploit.py).

Флаг: **ugra_zerobyte_does_not_count_9b0da3423e8d**.