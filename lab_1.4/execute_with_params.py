#! /usr/bin/python
# -*- coding: utf8 -*-

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-l",'--lang', type=str,
                    help= "Choose language abbreviation! (Ex. 'ua','en')")

parser.add_argument("-c", '--keyword', type=str,
                    help= "Choose word for filter! (Ex. 'hello')")

parser.add_argument(
	"-m", '--value',
	type=int,
    help="Choose number of the best moody for tweets! (Ex. '10', '-12')"
    )

args = parser.parse_args()

lang = args.lang
keyword = args.keyword
value = args.value


if __name__ == '__main__':
    print ('Parcer initialized! Please wait for filtering..')
    print (lang, keyword, value)
    input()
    
