#!/usr/bin/env python
# -*- coding: utf8 -*

import random
import numpy as np
from psychopy import visual
import copy

stim_text = {'CZERWONY': 'red', 'NIEBIESKI': '#5e75d9', 'BRAZOWY': '#574400', 'ZIELONY': 'green'}  # text: color
stim_neutral = "HHHHHHHH"
stim_distractor = ['WYSOKA', 'UKRYTA', u'GŁĘBOKA', 'DALEKA']

colors_text = list(stim_text.keys())
random.shuffle(colors_text)
colors_names = [stim_text[color] for color in colors_text]
left_hand = colors_text[:2]
right_hand = colors_text[2:]

last_text = None
last_text_2 = None
last_color = None


def prepare_trial(trial_type, win, text_height, words_dist):
    global last_color, last_text, last_text_2
    text = None
    stim_distr = None
    if trial_type == 'trial_con_con_con':
        possible_text = list(stim_text.keys())
        if last_text is not None:
            for elem in last_text:
                if elem in possible_text:
                    possible_text.remove(elem)
            try:
                possible_text.remove([k for k, v in stim_text.iteritems() if v == last_color][0])
            except:
                pass
        text = random.choice(possible_text)
        color = stim_text[text]
        words = [text, text, text]

    elif trial_type == 'trial_con_con_unr':
        possible_text = list(stim_text.keys())
        if last_text is not None:
            for elem in last_text:
                if elem in possible_text:
                    possible_text.remove(elem)
            try:
                possible_text.remove([k for k, v in stim_text.iteritems() if v == last_color][0])
            except:
                pass
        text = random.choice(possible_text)
        color = stim_text[text]
        possible_distr = copy.deepcopy(stim_distractor)
        if last_text_2 is not None:
            possible_distr.remove(last_text_2)
        stim_distr = random.choice(possible_distr)
        words = [text, text, stim_distr]

    elif trial_type == 'trial_con_unr_unr':
        possible_text = list(stim_text.keys())
        if last_text is not None:
            for elem in last_text:
                if elem in possible_text:
                    possible_text.remove(elem)
            try:
                possible_text.remove([k for k, v in stim_text.iteritems() if v == last_color][0])
            except:
                pass
        text = random.choice(possible_text)
        color = stim_text[text]
        possible_distr = copy.deepcopy(stim_distractor)
        if last_text_2 is not None:
            possible_distr.remove(last_text_2)
        stim_distr = random.choice(possible_distr)
        words = [text, stim_distr, stim_distr]

    elif trial_type == 'trial_inc_inc_inc':
        possible_text = list(stim_text.keys())
        if last_text is not None:
            for elem in last_text:
                if elem in possible_text:
                    possible_text.remove(elem)
        text = random.choice(possible_text)
        if text in left_hand:
            possible_colors = [stim_text[key] for key in right_hand]
        else:
            possible_colors = [stim_text[key] for key in left_hand]
        if last_color in possible_colors:
            possible_colors.remove(last_color)
        color = random.choice(possible_colors)
        words = [text, text, text]

    elif trial_type == 'trial_inc_inc_unr':
        possible_text = list(stim_text.keys())
        if last_text is not None:
            for elem in last_text:
                if elem in possible_text:
                    possible_text.remove(elem)
        text = random.choice(possible_text)
        if text in left_hand:
            possible_colors = [stim_text[key] for key in right_hand]
        else:
            possible_colors = [stim_text[key] for key in left_hand]
        if last_color in possible_colors:
            possible_colors.remove(last_color)
        color = random.choice(possible_colors)
        possible_distr = copy.deepcopy(stim_distractor)
        if last_text_2 is not None:
            possible_distr.remove(last_text_2)
        stim_distr = random.choice(possible_distr)
        words = [text, text, stim_distr]

    elif trial_type == 'trial_inc_unr_unr':
        possible_text = list(stim_text.keys())
        if last_text is not None:
            for elem in last_text:
                if elem in possible_text:
                    possible_text.remove(elem)
        text = random.choice(possible_text)
        if text in left_hand:
            possible_colors = [stim_text[key] for key in right_hand]
        else:
            possible_colors = [stim_text[key] for key in left_hand]
        if last_color in possible_colors:
            possible_colors.remove(last_color)
        color = random.choice(possible_colors)
        possible_distr = copy.deepcopy(stim_distractor)
        if last_text_2 is not None:
            possible_distr.remove(last_text_2)
        stim_distr = random.choice(possible_distr)
        words = [text, stim_distr, stim_distr]

    elif trial_type == 'trial_unr_unr_unr':
        possible_text = stim_distractor[:]
        if last_text is not None:
            for elem in last_text:
                if elem in possible_text:
                    possible_text.remove(elem)
        text = np.random.choice(possible_text)
        words = [text, text, text]
        possible_colors = list(stim_text.values())
        if last_color is not None:
            possible_colors.remove(last_color)
        color = random.choice(possible_colors)

    elif trial_type == 'trial_neu_neu_neu':
        text = stim_neutral
        words = [stim_neutral, stim_neutral, stim_neutral]
        possible_colors = list(stim_text.values())
        if last_color is not None:
            possible_colors.remove(last_color)
        color = random.choice(possible_colors)

    else:
        raise Exception('Wrong trigger type')

    random.shuffle(words)
    last_color = color
    last_text = text
    last_text_2 = stim_distr

    stim1 = visual.TextStim(win, color=color, text=words[0], height=text_height, pos=(0, words_dist))
    stim2 = visual.TextStim(win, color=color, text=words[1], height=text_height, pos=(0, 0))
    stim3 = visual.TextStim(win, color=color, text=words[2], height=text_height, pos=(0, -words_dist))
    # print({'trial_type': trial_type, 'text': words, 'color': color, 'stim': [stim1, stim2, stim3]})
    return {'trial_type': trial_type, 'text': words, 'color': color, 'stim': [stim1, stim2, stim3]}


def prepare_part(trials_con_con_con, trials_con_con_unr, trials_con_unr_unr,
                 trials_inc_inc_inc, trials_inc_inc_unr, trials_inc_unr_unr,
                 trials_unr_unr_unr, trials_neu_neu_neu,
                 win, text_height, words_dist):
    trials = ['trial_con_con_con'] * trials_con_con_con + \
             ['trial_con_con_unr'] * trials_con_con_unr + \
             ['trial_con_unr_unr'] * trials_con_unr_unr + \
             ['trial_inc_inc_inc'] * trials_inc_inc_inc + \
             ['trial_inc_inc_unr'] * trials_inc_inc_unr + \
             ['trial_inc_unr_unr'] * trials_inc_unr_unr + \
             ['trial_unr_unr_unr'] * trials_unr_unr_unr + \
             ['trial_neu_neu_neu'] * trials_neu_neu_neu
    random.shuffle(trials)
    return [prepare_trial(trial_type, win, text_height, words_dist) for trial_type in trials]


def prepare_exp(data, win, text_size, words_dist):
    text_height = 1.5 * text_size
    training1_trials = prepare_part(data['Training1_trials_con_con_con'],
                                    data['Training1_trials_con_con_unr'],
                                    data['Training1_trials_con_unr_unr'],
                                    data['Training1_trials_inc_inc_inc'],
                                    data['Training1_trials_inc_inc_unr'],
                                    data['Training1_trials_inc_unr_unr'],
                                    data['Training1_trials_unr_unr_unr'],
                                    data['Training1_trials_neu_neu_neu'],
                                    win, text_height, words_dist)

    training2_trials = prepare_part(data['Training2_trials_con_con_con'],
                                    data['Training2_trials_con_con_unr'],
                                    data['Training2_trials_con_unr_unr'],
                                    data['Training2_trials_inc_inc_inc'],
                                    data['Training2_trials_inc_inc_unr'],
                                    data['Training2_trials_inc_unr_unr'],
                                    data['Training2_trials_unr_unr_unr'],
                                    data['Training2_trials_neu_neu_neu'],
                                    win, text_height, words_dist)

    experiment_trials = prepare_part(data['Experiment_trials_con_con_con'],
                                     data['Experiment_trials_con_con_unr'],
                                     data['Experiment_trials_con_unr_unr'],
                                     data['Experiment_trials_inc_inc_inc'],
                                     data['Experiment_trials_inc_inc_unr'],
                                     data['Experiment_trials_inc_unr_unr'],
                                     data['Experiment_trials_unr_unr_unr'],
                                     data['Experiment_trials_neu_neu_neu'],
                                     win, text_height, words_dist)

    return [training1_trials, training2_trials], experiment_trials, colors_text, colors_names
