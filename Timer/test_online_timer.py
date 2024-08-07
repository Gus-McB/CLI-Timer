import unittest
import Agenda
import Clock
import CSV

class TestAgendaMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.agenda = Agenda.Agendas()
        self.task1 = 'name'
        self.agenda.addTask(self.task1)
        self.agenda.getAgenda()[0].timer.setTime(['0', '0', '30'])
       

    def testGetAgenda(self):
        self.assertIsInstance(self.agenda.getAgenda(), list)
    
    def testAddTask(self):
        self.agenda.addTask('newName')
        self.assertEqual(len(self.agenda.getAgenda()), 2)
    
    def testTimeAllocation(self):
        print("Time must be greater than 0.")
        self.agenda.timeAllocation()
        self.assertIsInstance(self.agenda.getAgenda()[0].timer.getTotal(), int)
        self.assertGreater(self.agenda.getAgenda()[0].timer.getTotal(), 0)
    
    def testRemoveTask(self):
        self.agenda.removeTask('name')
        self.assertIsInstance(self.agenda.getAgenda(), list)
        self.assertEqual(len(self.agenda.getAgenda()), 0)
    
    def TestEdit(self):
        self.agenda.edit("name", [1,1,1])
        self.assertEqual(self.agenda.getAgenda()[0], "name")
    
class TestClockMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.time = Clock.Timer()
    
    def testSetTime(self):
        self.time.setTime(['0', '0', '10'])
        self.assertEqual(self.time.getTotal(), 10)
    
    def testGetTime(self):
        self.assertEqual(self.time.getTotal(), 0)
    
class TestCSVMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.agenda = Agenda.Agendas()
        self.csv = CSV.CSVAccess('hello')
    
    def testImport(self):
        self.assertIsInstance(self.csv.timeImport("preset1"), list)

    def testTime(self):
        self.assertEqual(self.csv.Time("1:10:10"), ('1', '10', '10'))

if __name__ == '__main__':
    unittest.main()