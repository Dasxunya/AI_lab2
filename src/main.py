import functions as f
import colors as color

while True:
    try:
        print(color.BLUE)
        f.file_function(input('Введите имя файла:'))

    except KeyboardInterrupt:
        print(color.RED, '\n*Программа прервана :(*')
        exit(1)
    except FileNotFoundError:
        print(color.RED, "\n*Проверьте имя файла*")
    except:
        print(color.RED, '\n*Что-то пошло не так :(*')
