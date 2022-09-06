import datetime
from datetime import timedelta

time_format = '%H:%M'

class bus_stop:
    def __init__(self, name, wait_time, is_change_available):
        self.name = name
        self.wait_time = wait_time
        self.is_change_available = is_change_available


class position_on_route:
    def __init__(self, bus_stop, time_since_last_stop):
        self.bus_stop = bus_stop
        self.time_since_last_stop = time_since_last_stop


class route:
    def __init__(self, name, stops=[]):
        self.name = name
        self.stops = stops

    def add_bus_stop(self, bus_stop):
        self.stops.append(bus_stop)

    def get_finish_time(self, starting_time):

        for i in range(len(self.stops)):
            # I don't know if I should choose the time between stops or have user choose that, so I will just go with
            # 3 min
            temp = position_on_route(self.stops[i], 3)
            if i != 0:
                starting_time += timedelta(minutes=self.stops[i].wait_time)
                starting_time += timedelta(minutes=temp.time_since_last_stop)
        starting_time -= timedelta(minutes=self.stops[-1].wait_time)
        finish_time = starting_time
        return finish_time

    def print_route(self, starting_time):
        print("Route " + self.name + "\n")
        print("From " + str(self.stops[0].name) + " to " + str(self.stops[-1].name) + "\n")

        starting_time = datetime.datetime.strptime(starting_time, time_format)
        finish_time = self.get_finish_time(starting_time)

        print("Route starts at " + str(starting_time.time()) + " and ends at " + str(finish_time.time()))
        time = starting_time
        print("                            ARRIVAL          DEPARTURE       IS CHANGE AVAILABLE")
        for i in range(len(self.stops)):
            print("%25s" % self.stops[i].name + " - ", end='')
            temp = position_on_route(self.stops[i], 3)
            if i == 0:
                print("%25s" % str(starting_time.time()), end='')
                print("%20s" % (str(self.stops[i].is_change_available)))
            elif i + 1 == len(self.stops):
                print("%5s" % str(finish_time.time()), end='')
                print("%37s" % (str(self.stops[i].is_change_available)))
            else:
                time += timedelta(minutes=temp.time_since_last_stop)
                print("%5s" % str(time.time()) + "      -  ", end='')
                time += timedelta(minutes=self.stops[i].wait_time)
                print("%5s" % (str(time.time())), end='')
                print("%21s" % (str(self.stops[i].is_change_available)))


xd = route("525")

stop1 = bus_stop("Plac Narutowicza", 1, True)
stop2 = bus_stop("Rondo Daszyńskiego", 2, False)
stop3 = bus_stop("GUS", 4, False)
stop4 = bus_stop("Al. Jerozolimskie", 2, True)

xd.add_bus_stop(stop1)
xd.add_bus_stop(stop2)
xd.add_bus_stop(stop3)
xd.add_bus_stop(stop4)

xd.print_route('16:15')
