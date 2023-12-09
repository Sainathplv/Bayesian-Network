class bays(object):

    def init(self, values):
        return (self.sValue("B", values[0], None, None) * self.sValue("E", values[1], None, None) * self.sValue("A|B,E", values[2], values[0], values[1]) * self.sValue("J|A", values[3], values[2], None) * self.sValue("M|A", values[4], values[2], None))

    def nValue(self, values):
        if None in values:
            nns = values.index(None)
            nxt_itm = list(values)
            nxt_itm[nns] = True
            vl1 = self.nValue(nxt_itm)
            nxt_itm[nns] = False
            vl2 = self.nValue(nxt_itm)
            return vl1 + vl2
        else:
            return self.init(values)
# hardcoding of table values
    def sValue(self, val, val1, val2, val3):
        if val == "B":
            if val1:
                return 0.001
            else:
                return 0.999
        if val == "E":
            if val1:
                return 0.002
            else:
                return 0.998
        if val == "M|A":
            if val2:
                temp = 0.7
            else:
                temp = 0.01
            if val1:
                return temp
            else:
                return (1 - temp)
        if val == "J|A":
            if val2:
                temp = 0.9
            else:
                temp = 0.05
            if val1:
                return temp
            else:
                return (1 - temp)
        if val == "A|B,E":
            if val2 and val3:
                temp = 0.95
            if not val2 and not val3:
                temp = 0.001
            if val2 and not val3:
                temp = 0.94
            if not val2 and val3:
                temp = 0.29
            if val1:
                return temp
            else:
                return (1 - temp)

    def gtValue(self, vl):
        res = []
        if "Bf" in vl:
            res.append(False)
        elif "Bt" in vl:
            res.append(True)
        else:
            res.append(None)
        if "Ef" in vl:
            res.append(False)
        elif "Et" in vl:
            res.append(True)
        else:
            res.append(None)
        if "Af" in vl:
            res.append(False)
        elif "At" in vl:
            res.append(True)
        else:
            res.append(None)
        if "Jf" in vl:
            res.append(False)
        elif "Jt" in vl:
            res.append(True)
        else:
            res.append(None)
        if "Mt" in vl:
            res.append(True)
        elif "Mf" in vl:
            res.append(False)
        else:
            res.append(None)

        return res
