#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_card
----------------------------------

Tests for `python_card_game` module.

Check-out this tutorial on Unit Testing in Python

https://cgoldberg.github.io/python-unittest-tutorial/

"""

import unittest

from python_card_game.engine import Card, BadCardParamsExepction


def card_setup_runner(setup_dict):
  c = None
  try:
    c = Card(**setup_dict)
  except BadCardParamsExepction as e:
    pass
    # print "got BadCardParamsExepction on test 1"
    # return True
  except Exception as e:
    raise
  return c


class TestCard(unittest.TestCase):

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_card_defaults(self):
    caught_exception = False
    try:
      Card()
    except BadCardParamsExepction as e:
      # print "got BadCardParamsExepction on test 0"
      caught_exception = True
    else:
      pass
    finally:
      pass

    # self.assertIsNotNone(c, msg='failure in Card default constructor')
    self.assertTrue(caught_exception, msg='failure in Card constructor for default configuration')

  def test_card_simple(self):
    card_setup = {
        "gold": 0,
        "diplomacy": 0,
        "stealth": 1,
        "might": 1,
        "victory_point": 2,
        "effect": "None",
    }

    # caught_exception = False
    # try:
    #   c = Card(**card_setup)
    # except BadCardParamsExepction as e:
    #   # print "got BadCardParamsExepction on test 1"
    #   caught_exception = True
    # except Exception as e:
    #   raise
    c = card_setup_runner(card_setup)
    self.assertIsNotNone(c, msg='failure in Card constructor for simple configuration')

  def test_card_exception_bad_attr(self):
    # tests for individual attribute value greater than its particular max
    card_setup = {
        "gold": 0,
        "diplomacy": 0,
        "stealth": 10,
        "might": 0,
        "victory_point": 2,
        "effect": "None",
    }
    # TODO: DREW you fill in this one
    caught_exception = False
    try:
      c = Card(**card_setup)
    except BadCardParamsExepction as e:
      # print "got BadCardParamsExepction on test 2"
      caught_exception = True
    except Exception as e:
      raise

    self.assertTrue(caught_exception, msg="Failed to catch bad attribute exception")

  def test_card_exception_attr_sum(self):
    # tests for card_sum(more than 6)
    card_setup = {
        "gold": 0,
        "diplomacy": 4,
        "stealth": 4,
        "might": 0,
        "victory_point": 2,
        "effect": "None",
    }
    # TODO: DREW you fill in this one
    caught_exception = False
    try:
      c = Card(**card_setup)
    except BadCardParamsExepction as e:
      # print "got BadCardParamsExepction on test 3"
      caught_exception = True
    except Exception as e:
      raise

    self.assertTrue(caught_exception, msg="Failed to catch attribute sum more than 6")

  def test_card_exception_even_sum(self):
    # tests for even resources
    card_setup = {
        "gold": 0,
        "diplomacy": 3,
        "stealth": 2,
        "might": 0,
        "victory_point": 2,
        "effect": "None",
    }

    caught_exception = False
    try:
      c = Card(**card_setup)
    except BadCardParamsExepction as e:
      # print "got BadCardParamsExepction on test 4"
      caught_exception = True
    except Exception as e:
      raise

    self.assertTrue(caught_exception, msg="Failed to catch even sum exception")

  def test_card_exception_non_zero_count(self):
    card_setup = {
        "gold": 0,
        "diplomacy": 1,
        "stealth": 2,
        "might": 3,
        "victory_point": 2,
        "effect": "None",
    }
    caught_exception = False
    try:
      c = Card(**card_setup)
    except BadCardParamsExepction as e:
      # print "got BadCardParamsExepction on test 5"
      caught_exception = True
    except Exception as e:
      raise

    self.assertTrue(caught_exception, msg="Failed to catch non_zero_count exception")

if __name__ == '__main__':
  import sys
  sys.exit(unittest.main())
