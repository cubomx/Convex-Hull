def order(points, toAdd):
    events = sorted(points, reverse=False, key=lambda x: x.coords[1])
    i = 0
    while i + 1 < len(events):
        if events[i].coords[1] == events[i + 1].coords[1]:
            if events[i].coords[0] > events[i + 1].coords[0]:
                aux = events[i]
                events[i] = events[i + 1]
                events[i + 1] = aux
                i = 0
            elif events[i].coords[0] == events[i + 1].coords[0] and toAdd:
                events[i].insert_segment(events[i + 1].get_seg(0))
                events.remove(events[i + 1])

        i += 1
    return events

