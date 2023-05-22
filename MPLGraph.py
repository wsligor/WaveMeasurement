import sqlite3 as sl

from matplotlib import pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MPLGraph(FigureCanvasQTAgg):

    def __init__(self):
        fig = Figure(layout='constrained')
        self.axes = fig.add_subplot(111)
        super().__init__(fig)
        self.style = "seaborn-v0_8-whitegrid"
        self.title = "Wave measurement"

    # TODO Провести рефакторинг кода функции
    def plot(self, selectsRowNameExp):
        self.axes.clear()
        self.axes.grid(color='gray', linewidth=0.5, linestyle='-')
        self.axes.set_title(self.title)
        self.axes.set_xlabel("waveLength")
        self.axes.set_ylabel("transparency")

        con = sl.connect('SFM.db')
        cur = con.cursor()
        sql = f'''SELECT waveLength FROM dataExp WHERE id_nameExp = {30} and waveLength > 300'''
        cur.execute(sql)
        rows = cur.fetchall()
        x = [r[0] for r in rows]

        for sel in selectsRowNameExp:
            sql = f'''SELECT transparency FROM dataExp WHERE id_nameExp = {sel} and waveLength > 300'''
            cur.execute(sql)
            collumns = cur.fetchall()
            y = [c[0] for c in collumns]
            self.axes.plot(x, y)
            # y.clear()

        con.commit()
        self.draw()
        pass

    def plot_meam(self, lset, a_meam):
        with plt.style.context(self.style):
            if self.ax:
                self.fig.delaxes(self.ax)
            self.ax = self.fig.add_subplot(1, 1, 1)
            self.ax.grid(color='gray', linewidth=0.5, linestyle='-')
            # self.ax.set_xlim(290, 1010)  # мин и мах координаты х
            # self.ax.set_ylim(94, 107)  # мин и мах координаты y
            self.ax.set_title(self.title)
            self.ax.set_xlabel("waveLength")
            self.ax.set_ylabel("transparency")
            for id in lset:
                id_x = id
                continue
            x = []
            y = []
            con = sl.connect('SFM.db')
            cur = con.cursor()
            sql = '''SELECT waveLength FROM dataExp WHERE id_nameExp = {} and waveLength > 300'''.format(id_x)
            cur.execute(sql)
            rows = cur.fetchall()
            for i in rows:
                x.append(i[0])


            for l in lset:
                sql = '''SELECT transparency FROM dataExp WHERE id_nameExp = {} and waveLength > 300'''.format(l)
                cur.execute(sql)
                collumns = cur.fetchall()
                for i in collumns:
                    y.append(i[0])
                self.ax.plot(x, y)
                y.clear()

            self.ax.plot(x, a_meam)

            con.commit()
            self.draw()
