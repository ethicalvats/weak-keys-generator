import codecs

import eth_address
import bigquery


def fetch_transactions(address):
    result = bigquery.make(address)
    print("Transactions")
    for row in result:
        print(row)


def gen_eth_address(key):
    address = eth_address.gen(key[2:])
    print("Ethereum Address")
    print(address)
    # fetch_transactions(address)


def gen_private_keys(start, end):
    padding = 66
    for i in range(start, end + 1):
        key = f"{i:#0{padding}x}"
        gen_eth_address(key)


def gen_group_A():
    start = 0x0000000000000000000000000000000000000000000000000000000000000001
    end = 0x00000000000000000000000000000000000000000000000000000000FFFFFFFF
    gen_private_keys(start, end)


def gen_group_B():
    start = 0x0000000000000000000000000000000000000000000000000000000100000000
    end = 0x000000000000000000000000000000000000000000000000FFFFFFFF00000000
    gen_private_keys(start, end)


def gen_group_C():
    start = 0x0000000000000000000000000000000000000000000000010000000000000000
    end = 0x0000000000000000000000000000000000000000FFFFFFFF0000000000000000
    gen_private_keys(start, end)


def gen_group_D():
    start = 0x0000000000000000000000000000000000000001000000000000000000000000
    end = 0x00000000000000000000000000000000FFFFFFFF000000000000000000000000
    gen_private_keys(start, end)


def gen_group_E():
    start = 0x0000000000000000000000000000000100000000000000000000000000000000
    end = 0x000000000000000000000000FFFFFFFF00000000000000000000000000000000
    gen_private_keys(start, end)


def gen_group_F():
    start = 0x0000000000000000000000010000000000000000000000000000000000000000
    end = 0x0000000000000000FFFFFFFF0000000000000000000000000000000000000000
    gen_private_keys(start, end)


def gen_group_G():
    start = 0x0000000000000001000000000000000000000000000000000000000000000000
    end = 0x00000000FFFFFFFF000000000000000000000000000000000000000000000000
    gen_private_keys(start, end)


def gen_group_H():
    start = 0x0000000100000000000000000000000000000000000000000000000000000000
    end = 0xFFFFFFFF00000000000000000000000000000000000000000000000000000000
    gen_private_keys(start, end)


def gen_weak_keys():
    gen_group_A()
    gen_group_B()
    gen_group_C()
    gen_group_D()
    gen_group_E()
    gen_group_F()
    gen_group_G()
    gen_group_H()


if __name__ == "__main__":
    gen_weak_keys()
