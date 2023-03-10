'''
Основные шаги симуляции
Вот основная модель.

1 Создать очередь из заданий на печать. Каждое из них будет иметь отметку о
  времени постановки в очередь. В самом начале очередь пуста.
2 Для каждой секунды (currentSecond):
    * Создано ли новое задание на печать? Если да, то добавить его в очередь с
     currentSecond в качестве отметки времени.
    * Если принтер не занят и есть ожидающее задание, то
        Удалить следующее задание из очереди на печать и передать его принтеру.
        Извлечь отметку о времени из currentSecond чтобы вычислить время ожидания для данного задания.
        Добавить время ожидания этой задачи в список для дальнейшей обработки.
        Основываясь на количестве страниц в задании на печать, вычислить, сколько для него потребуется времени.
    * Если необходимо, принтер тратит одну секунду печати. Также он вычитает
        её из времени, необходимого для выполнения задачи.
    * Если задание завершено (другими словами, требуемое на его выполнение время
 равно нулю), то принтер более не занят.
3 После завершения симуляции вычисляется среднее время ожидания из
сгенерированного списка времён ожидания.
'''
import random
import queue_exsampl


class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        # текущее задание
        self.currentTask = None
        # Оставшиеся время
        self.timeRemaining = 0

    def tick(self):
        """Кол-во печатаемых в минуту страниц"""
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, curenttime):
        return curenttime - self.timestamp


def simulation(numSeconds, pagesPerMinute):

    labprinter = Printer(pagesPerMinute)
    printQueue = queue_exsampl.Queue()
    waitingtimes = []

    for currentSeconds in range(numSeconds):
        if newPrintTask():
            task = Task(currentSeconds)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSeconds))
            labprinter.startNext(nexttask)

        labprinter.tick()

    averageWait = sum(waitingtimes) / len(waitingtimes)
    print(
        f"Average Wait {averageWait} secs {printQueue.size()} tasks remaining."
    )


def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


# if __name__ == '__main__':
for i in range(10):
    simulation(3600,5)