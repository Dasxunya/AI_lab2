# AI_lab2
Цель задания: Исследование алгоритмов решения задач методом поиска.
Описание предметной области. Имеется транспортная сеть, связывающая
города СНГ. Сеть представлена в виде таблицы связей между городами. Связи
являются двусторонними, т.е. допускают движение в обоих направлениях.
Необходимо проложить маршрут из одной заданной точки в другую.

**Этап 1. Неинформированный поиск. На этом этапе известна только
топология связей между городами. Выполнить:**

- [X] поиск в ширину;
- [X] поиск глубину;
- [X] поиск с ограничением глубины;
- [X] поиск с итеративным углублением;
- [X] двунаправленный поиск.
Отобразить движение по дереву на его графе с указанием сложности
каждого вида поиска. Сделать выводы.

**Этап 2. Информированный поиск. Воспользовавшись информацией о
протяженности связей от текущего узла, выполнить:**

- [X] жадный поиск по первому наилучшему соответствию;
- [X] затем, использую информацию о расстоянии до цели по прямой от
каждого узла, выполнить поиск методом минимизации суммарной оценки
А*. 
