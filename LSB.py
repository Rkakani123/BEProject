class SteganographyException(Exception):
    pass

class LSB():

    def __init__(self, im, ind):
        self.image = im
        self.index = ind
        self.size = len(ind)
        self.i = 0
        self.j = 0

    def put_binary_value(self, bits):

        for c in bits:
            val = list(self.image[self.index[self.i][0], self.index[self.i][1]])
            if int(c) == 1:
                self.image[self.index[self.i][0], self.index[self.i][1]][self.j] = int(val[self.j]) | 1
            else:
                self.image[self.index[self.i][0], self.index[self.i][1]][self.j] = int(val[self.j]) & 254
            self.next_slot()

    def put_binary_value_1(self, bits):

        for c in bits:
            val = list(self.image[self.index[self.i][0], self.index[self.i][1]])
            if int(c) == 1:
                self.image[self.index[self.i][0], self.index[self.i][1]][self.j] = int(val[self.j]) | 2
            else:
                self.image[self.index[self.i][0], self.index[self.i][1]][self.j] = int(val[self.j]) & 253
            self.next_slot()

    def next_slot(self):
        if self.j == 2:
            self.j = 0
            if self.i >= self.size:
                raise SteganographyException("Sufficien space is not available to store information.")
            else:
                self.i += 1
        else:
            self.j += 1

    def read_bit(self):
        val = self.image[self.index[self.i][0], self.index[self.i][1]][self.j]
        val = int(val) & 1
        self.next_slot()
        if val > 0:
            return "1"
        else:
            return "0"

    def read_bit_1(self):
        val = self.image[self.index[self.i][0], self.index[self.i][1]][self.j]
        val = int(val) & 2
        self.next_slot()
        if val > 0:
            return "1"
        else:
            return "0"

    def read_bits(self, nb):
        bits = ""
        for i in range(nb):
            bits += self.read_bit()
        return bits

    def read_bits_1(self, nb):
        bits = ""
        for i in range(nb):
            bits += self.read_bit_1()
        return bits

    def byteValue(self, val):
        return self.binary_value(val, 8)

    def binary_value(self, val, bitsize):
        binval = bin(val)[2:]
        if len(binval) > bitsize:
            raise SteganographyException("binary value larger than the expected size")
        while len(binval) < bitsize:
            binval = "0" + binval

        return binval

    def encode_text(self, txt):
        l = len(txt)
        binl = self.binary_value(l, 16)
        self.put_binary_value(binl)
        count = 0
        for char in txt:
            c = ord(char)
            if (count % 2 == 0):
                self.put_binary_value(self.byteValue(c))
            else:
                self.put_binary_value_1(self.byteValue(c))
            count += 1
        return self.image

    def decode_text(self):
        ls = self.read_bits(16)
        l = int(ls, 2)
        i = 0
        unhideTxt = ""
        while i < l:
            if (i % 2 == 0):
                tmp = self.read_bits(8)
            else:
                tmp = self.read_bits_1(8)
            i += 1
            unhideTxt += chr(int(tmp, 2))
        return unhideTxt