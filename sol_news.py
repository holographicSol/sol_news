""" Written by Benjamin Jack Cullen - All rights reserved."""

import os
import distutils.dir_util
import time
import datetime
import requests
from bs4 import BeautifulSoup
import codecs
from colorama import Fore, Back, Style


encode = u'\u5E73\u621015\u200e'

debug_mode = False
char_limit = 173
dir_now = ''
tm_stamp = ''
history = []

meteo_hud_eq = []
meteo_hud_tc = []
meteo_hud_fl = []
meteo_hud_vo = []
meteo_hud_dr = []
meteo_hud_wf = []
defcon_hud = ''
doomday_hud = ''
nasa_climate_data = []


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def clear_console_line():
    print(' '*char_limit, end='\r', flush=True)


def pr_technical_data(technical_data):
    technical_data = technical_data[:char_limit]
    print(technical_data, end='\r', flush=True)


def make_dirs():
    dat_dir = './news_articles'
    distutils.dir_util.mkpath(dat_dir)
    dat_dir_1 = './extra_data'
    distutils.dir_util.mkpath(dat_dir_1)


def sol_news():
    global debug_mode, dir_now, tm_stamp
    global meteo_hud_eq
    global meteo_hud_tc
    global meteo_hud_fl
    global meteo_hud_vo
    global meteo_hud_dr
    global meteo_hud_wf
    global defcon_hud, doomday_hud
    global nasa_climate_data

    clear_console()

    try:
        time_now = str(datetime.datetime.now())
        time_now = time_now.replace(':', '-')
        time_now = time_now.replace('.', '')
        tm_stamp = time_now.replace(' ', '_')
        dir_now = './news_articles/' + tm_stamp + '/'
        distutils.dir_util.mkpath(dir_now)

    except Exception as e:
        clear_console_line()
        technical_data = str('[Time Now:' + str(datetime.datetime.now()) + ' Issue Time:' + str(tm_stamp) + '] ' + str(e) + '. reattempting in 1 second')
        if debug_mode is False:
            pr_technical_data(technical_data)
        else:
            print(technical_data)
        time.sleep(1)
        sol_news()

    print(Style.BRIGHT + Back.RED + str(' ' * char_limit) + Style.RESET_ALL)
    print('')
    hud_data_title = 'METEOROLOGICAL DATA - GLOBAL DISASTER ALERT COORDINATION SYSTEM'
    hud_data_title_pos = int((char_limit / 2) - (len(hud_data_title) / 2))
    print(str(' ' * hud_data_title_pos) + Style.BRIGHT+Fore.CYAN+hud_data_title+Style.RESET_ALL)
    print('')

    hud_limit = 5

    try:
        i = 0
        for _ in meteo_hud_eq:
            if i < hud_limit and len(meteo_hud_eq) >= i:
                print(str(_))
            i += 1

        i = 0
        for _ in meteo_hud_tc:
            if i < hud_limit and len(meteo_hud_tc) >= i:
                print(str(_))
            i += 1

        i = 0
        for _ in meteo_hud_fl:
            if i < hud_limit and len(meteo_hud_fl) >= i:
                print(str(_))
            i += 1

        i = 0
        for _ in meteo_hud_vo:
            if i < hud_limit and len(meteo_hud_vo) >= i:
                print(str(_))
            i += 1

        i = 0
        for _ in meteo_hud_dr:
            if i < hud_limit and len(meteo_hud_dr) >= i:
                print(str(_))
            i += 1

        i = 0
        for _ in meteo_hud_wf:
            if i < hud_limit and len(meteo_hud_wf) >= i:
                print(str(_))
            i += 1

        print('')
        print(Style.BRIGHT + Back.RED + str(' ' * char_limit) + Style.RESET_ALL)
        print('')
        hud_data_title = 'DEFCON WARNING SYSTEM AND DOOMSDAY CLOCK'
        hud_data_title_pos = int((char_limit / 2) - (len(hud_data_title) / 2))
        print(str(' ' * hud_data_title_pos) + Style.BRIGHT + Fore.CYAN + hud_data_title + Style.RESET_ALL)
        print('')
        print(defcon_hud)
        print(doomday_hud)

        print('')
        print(Style.BRIGHT + Back.RED + str(' ' * char_limit) + Style.RESET_ALL)
        print('')
        hud_data_title = 'NASA CLIMATE CHANGE - VITAL SIGNS OF THE PLANET'
        hud_data_title_pos = int((char_limit / 2) - (len(hud_data_title) / 2))
        print(str(' ' * hud_data_title_pos) + Style.BRIGHT + Fore.CYAN + hud_data_title + Style.RESET_ALL)
        print('')

        max_nasa_climate_data_len = []
        max_nasa_climate_data_len_1 = []
        max_nasa_climate_data_len.append(len(nasa_climate_data[0]))
        max_nasa_climate_data_len.append(len(nasa_climate_data[1]))
        max_nasa_climate_data_len.append(len(nasa_climate_data[2]))
        max_nasa_climate_data_len.append(len(nasa_climate_data[3]))
        max_nasa_climate_data_len.append(len(nasa_climate_data[4]))
        max_nasa_climate_data_len.append(len(nasa_climate_data[5]))
        max_nasa_climate_data_len_fin = max(max_nasa_climate_data_len)
        max_nasa_climate_data_len_fin += 4

        max_nasa_climate_data_len_1.append(len(nasa_climate_data[1]))
        max_nasa_climate_data_len_1.append(len(nasa_climate_data[4]))
        max_nasa_climate_data_len_fin_1 = max(max_nasa_climate_data_len_1)
        max_nasa_climate_data_len_fin_1 += 4

        print(nasa_climate_data[0] + str(' '*(max_nasa_climate_data_len_fin - len(nasa_climate_data[0]))) + str(nasa_climate_data[1]) + str(' '*(max_nasa_climate_data_len_fin_1 - len(nasa_climate_data[1]))) + str(nasa_climate_data[2]))
        print(nasa_climate_data[3] + str(' ' *(max_nasa_climate_data_len_fin - len(nasa_climate_data[3]))) + str(nasa_climate_data[4]) + str(' '*(max_nasa_climate_data_len_fin_1 - len(nasa_climate_data[4]))) + str(nasa_climate_data[5]))

        print('')
        print(Style.BRIGHT + Back.RED + str(' ' * char_limit) + Style.RESET_ALL)
        print('')
        print(Style.BRIGHT + Fore.CYAN + 'TECHNICHAL DATA' + Style.RESET_ALL)
        print('')

        print('[' + str(datetime.datetime.now()) + '] -- performing data scan', end='\r', flush=True)
        funk_0()
        funk_1()
        funk_2()
        funk_3()
        funk_4()
        funk_5()
        funk_6()
        funk_7()
        funk_8()
        funk_9()

    except Exception as e:
        clear_console_line()
        technical_data = str('[Time Now:' + str(datetime.datetime.now()) + ' Issue Time:' + str(tm_stamp) + '] ' + str(e) + '. reattempting in 1 second')
        if debug_mode is False:
            pr_technical_data(technical_data)
        else:
            print(technical_data)
        time.sleep(1)
        sol_news()

    try:
        if len(os.listdir(path=dir_now)) == 0:
            os.rmdir(dir_now)
    except Exception as e:
        clear_console_line()
        technical_data = str('[Time Now:' + str(datetime.datetime.now()) + ' Issue Time:' + str(tm_stamp) + '] ' + str(e) + '. reattempting in 1 second')
        if debug_mode is False:
            pr_technical_data(technical_data)
        else:
            print(technical_data)
        time.sleep(1)
        sol_news()


def funk_extras():
    global debug_mode, defcon_hud, doomday_hud, tm_stamp
    try:
        clear_console_line()
        url = 'https://www.defconlevel.com/current-level.php'
        print('[' + str(datetime.datetime.now()) + '] -- scanning defcon level:', url, end='\r', flush=True)

        defcon_level = ''
        defcon_level_data = ''
        rHead = requests.get(url)
        data = rHead.text
        soup = BeautifulSoup(data, "html.parser")
        for row in soup.find_all():
            text = row.get_text()
            if text.startswith('Overall Current Defcon Level Today: '):
                text = str(text).split()
                for _ in text:
                    if _.isdigit():
                        defcon_level = _

                if defcon_level == '1':
                    toFile = str('[Defcon Level] [' + defcon_level + '] [Cocked Pistol] [Nuclear Threat is Either in Progress or Imminent] [Maximum Readiness]')
                    defcon_level_data = '[' + Style.BRIGHT+Fore.LIGHTWHITE_EX+'Defcon Level'+Style.RESET_ALL + '] ' + '[' + Style.BRIGHT+Fore.LIGHTWHITE_EX+str(defcon_level)+Style.RESET_ALL + '] [' + Style.BRIGHT+Fore.LIGHTWHITE_EX+'Cocked Pistol'+Style.RESET_ALL + '] [' + Style.BRIGHT+Fore.LIGHTWHITE_EX+'Nuclear Threat is Either in Progress or Imminent'+Style.RESET_ALL + '] [' + Style.BRIGHT+Fore.LIGHTWHITE_EX+'Maximum Readiness'+Style.RESET_ALL + ']'
                elif defcon_level == '2':
                    toFile = str('[Defcon Level] [' + defcon_level + '] [Fast Pace] [At the Next Step to War or Nuclear Threat] [Penultimate Readiness]')
                    defcon_level_data = '[' + Style.BRIGHT+Fore.RED + 'Defcon Level' + Style.RESET_ALL + '] ' + '[' + Style.BRIGHT+Fore.RED + str(defcon_level) + Style.RESET_ALL + '] [' + Style.BRIGHT+Fore.RED + 'Fast Pace' + Style.RESET_ALL + '] [' + Style.BRIGHT+Fore.RED + 'At the Next Step to War or Nuclear Threat' + Style.RESET_ALL + '] [' + Style.BRIGHT+Fore.RED + 'Penultimate Readiness' + Style.RESET_ALL + ']'
                elif defcon_level == '3':
                    toFile = str('[Defcon Level] [' + defcon_level + '] [Round House] [Prepared Cautious in High State of Readiness] [Higher Level Readiness]')
                    defcon_level_data = '[' + Style.BRIGHT+Fore.YELLOW + 'Defcon Level'+Style.RESET_ALL+'] ' + '[' + Style.BRIGHT+Fore.YELLOW + str(defcon_level) + Style.RESET_ALL + '] [' + Style.BRIGHT+Fore.YELLOW + 'Round House' + Style.RESET_ALL + '] [' + Style.BRIGHT+Fore.YELLOW + 'Prepared Cautious in High State of Readiness' + Style.RESET_ALL + '] [' + Style.BRIGHT+Fore.YELLOW + 'Higher Level Readiness' + Style.RESET_ALL + ']'
                elif defcon_level == '4':
                    toFile = str('[Defcon Level] [' + defcon_level + '] [Double Take] [Intel Gathering & Strengthening of Security] [Above Normal Readiness]')
                    defcon_level_data = '[' + Style.BRIGHT+Fore.GREEN + 'Defcon Level' + Style.RESET_ALL + '] ' + '[' + Style.BRIGHT+Fore.GREEN + str(defcon_level) + Style.RESET_ALL + '] [' + Style.BRIGHT+Fore.GREEN + 'Double Take' + Style.RESET_ALL + '] [' + Style.BRIGHT+Fore.GREEN + 'Intel Gathering & Strengthening of Security' + Style.RESET_ALL + '] [' + Style.BRIGHT+Fore.GREEN + 'Above Normal Readiness' + Style.RESET_ALL + ']'
                elif defcon_level == '5':
                    toFile = str('[Defcon Level] [' + defcon_level + '] [Fade Out] [Complete and Total State of Peace] [Lowest Level Readiness]')
                    defcon_level_data = '[' + Style.BRIGHT+Fore.CYAN + 'Defcon Level' + Style.RESET_ALL + '] ' + '[' + Style.BRIGHT+Fore.CYAN + str(defcon_level) + Style.RESET_ALL + '] [' + Style.BRIGHT+Fore.CYAN + 'Fade Out' + Style.RESET_ALL + '] [' + Style.BRIGHT+Fore.CYAN + 'Complete and Total State of Peace' + Style.RESET_ALL + '] [' + Style.BRIGHT+Fore.CYAN + 'Lowest Level Readiness' + Style.RESET_ALL + ']'

                defcon_hud = defcon_level_data

                target_line = ''
                if os.path.exists('./extra_data/extra_information.txt'):
                    with open('./extra_data/extra_information.txt', 'r') as fo:
                        for line in fo:
                            line = line.strip()
                            if 'Defcon Level' in line:
                                target_line = line
                if toFile not in target_line:
                    with codecs.open('./extra_data/extra_information.txt', 'a', encoding="UTF-8") as fo:
                        fo.write('[' + str(datetime.datetime.now()) + '] ' + toFile + '\n')
                    fo.close()
    except Exception as e:
        clear_console_line()
        technical_data = str('[Time Now:' + str(datetime.datetime.now()) + ' Issue Time:' + str(tm_stamp) + '] ' + str(e) + '. reattempting in 1 second')
        if debug_mode is False:
            pr_technical_data(technical_data)
        else:
            print(technical_data)
        time.sleep(1)
        funk_extras()
    try:
        clear_console_line()
        url = 'https://www.defconlevel.com/doomsday-clock.php'
        print('[' + str(datetime.datetime.now()) + '] -- scanning doomsday clock:', url, end='\r', flush=True)

        rHead = requests.get(url)
        data = rHead.text
        soup = BeautifulSoup(data, "html.parser")
        for row in soup.find_all():
            text = row.get_text()
            if text.endswith(' To Midnight'):
                text = '[' + Style.BRIGHT+Fore.RED+'Doomsday Clock ' + str(text).replace('Doomsday Clock', '') + Style.RESET_ALL+ ']'
                doomday_hud = text
                target_line = ''
                if os.path.exists('./extra_data/extra_information.txt'):
                    with open('./extra_data/extra_information.txt', 'r') as fo:
                        for line in fo:
                            line = line.strip()
                            if 'Doomsday Clock' in line:
                                target_line = line
                if text not in target_line:
                    with codecs.open('./extra_data/extra_information.txt', 'a', encoding="UTF-8") as fo:
                        fo.write('[' + str(datetime.datetime.now()) + '] ' + text + '\n')
                    fo.close()
    except Exception as e:
        clear_console_line()
        technical_data = str('[Time Now:' + str(datetime.datetime.now()) + ' Issue Time:' + str(tm_stamp) + '] ' + str(e) + '. reattempting in 1 second')
        if debug_mode is False:
            pr_technical_data(technical_data)
        else:
            print(technical_data)
        time.sleep(1)
        funk_extras()


def meteorological_data():
    global debug_mode, tm_stamp, meteo_hud_eq, meteo_hud_tc, meteo_hud_fl, meteo_hud_vo, meteo_hud_dr, meteo_hud_wf

    try:
        dat_file = './extra_data/global_disaster_alert_coord_system.txt'

        title = []
        descript = []
        iscurrent = []
        fromdate = []
        todate = []
        durationinweek = []
        eventtype = []
        alertlevel = []
        severity = []
        population = []
        country = []
        eventname = []

        meteo_hud_eq = []
        meteo_hud_tc = []
        meteo_hud_fl = []
        meteo_hud_vo = []
        meteo_hud_dr = []
        meteo_hud_wf = []

        clear_console_line()
        url = 'https://www.gdacs.org/xml/rss.xml'
        technical_data = str('[' + str(datetime.datetime.now()) + '] -- scanning meteorological data: ' + url)
        pr_technical_data(technical_data)

        rHead = requests.get(url)
        data = rHead.text
        soup = BeautifulSoup(data, "html.parser")
        for _ in soup.find_all('title'):
            if _ is not None:
                # print(_)
                var_0 = str(_).replace('<title>', '').replace('</title>', '')
                title.append(var_0)
        for _ in soup.find_all('description'):
            if _ is not None:
                # print(_)
                var_0 = str(_).replace('<description>', '').replace('</description>', '')
                descript.append(var_0)
        for _ in soup.find_all('gdacs:iscurrent'):
            if _ is not None:
                # print(_)
                var_0 = str(_).replace('<gdacs:iscurrent>', '').replace('</gdacs:iscurrent>', '')
                iscurrent.append(var_0)
        for _ in soup.find_all('gdacs:fromdate'):
            if _ is not None:
                # print(_)
                var_0 = str(_).replace('<gdacs:fromdate>', '').replace('</gdacs:fromdate>', '').replace(',', '')
                var_0 = var_0[4:]
                fromdate.append(var_0)
        for _ in soup.find_all('gdacs:todate'):
            if _ is not None:
                # print(_)
                var_0 = str(_).replace('<gdacs:todate>', '').replace('</gdacs:todate>', '')
                todate.append(var_0)
        for _ in soup.find_all('gdacs:durationinweek'):
            if _ is not None:
                # print(_)
                var_0 = str(_).replace('<gdacs:durationinweek>', 'Duration Weeks:').replace('</gdacs:durationinweek>', '').replace('Duration Weeks', 'Weeks')
                durationinweek.append(var_0)
        for _ in soup.find_all('gdacs:eventtype'):
            if _ is not None:
                # print(_)
                var_0 = str(_).replace('<gdacs:eventtype>', '').replace('</gdacs:eventtype>', '')
                eventtype.append(var_0)
        for _ in soup.find_all('gdacs:alertlevel'):
            if _ is not None:
                # print(_)
                var_0 = str(_).replace('<gdacs:alertlevel>', '').replace('</gdacs:alertlevel>', '')
                alertlevel.append(var_0)

        for _ in soup.find_all('gdacs:severity'):
            if _ is not None:
                # print(_)
                var_0 = str(_).replace('<gdacs:severity unit="M" value="', '').replace('</gdacs:severity>', '')  # EQ
                idx = var_0.find('>')
                var_0 = var_0[idx+1:]
                var_0 = var_0.replace('M,', ' ').replace('Magnitude ', 'Magnitude:').replace(' Depth:', 'Depth:')
                if var_0 == '':
                    var_0 = 'Severity: no data'
                severity.append(var_0)
        for _ in soup.find_all('gdacs:population'):
            if _ is not None:
                # print(_)
                var_0 = str(_).replace('<gdacs:population unit="', '').replace('</gdacs:population>', '').replace('" value="', ':').replace('" value="', ':')  #.replace('Population in', 'Pop.').replace('Pop74', 'Pop.').replace('Population Affected', 'Affect.Pop')  # POPULATION
                idx = var_0.find('>')
                var_0 = var_0[idx+1:]
                if var_0 == '':
                    var_0 = 'Population: no data'
                population.append(var_0)
        for _ in soup.find_all('gdacs:country'):
            if _ is not None:
                # print(_)
                var_0 = str(_).replace('<gdacs:country>', '').replace('</gdacs:country>', '')
                if var_0 == '':
                    var_0 = 'Off Shore'
                country.append(var_0)
        for _ in soup.find_all('gdacs:eventname'):
            if _ is not None:
                # print(_)
                var_0 = str(_).replace('<gdacs:eventname>', '').replace('</gdacs:eventname>', '')
                eventname.append(var_0)

        del title[0]
        del descript[0]

        hud_count_eq = 0
        hud_count_tc = 0
        hud_count_fl = 0
        hud_count_vo = 0
        hud_count_dr = 0
        hud_count_wf = 0
        hud_event_type_limit = [0, 1, 2, 3, 4, 5]

        i = 0
        for _ in title:

            col_res = Style.RESET_ALL
            txt_col = Style.RESET_ALL

            if 'Red' in alertlevel[i]:
                txt_col = Style.BRIGHT+Fore.RED
            elif 'Orange' in alertlevel[i]:
                txt_col = Style.BRIGHT+Fore.YELLOW
            elif 'Green' in alertlevel[i]:
                txt_col = Style.BRIGHT+Fore.GREEN

            if str(eventtype[i]) == 'EQ':
                if hud_count_eq in hud_event_type_limit:
                    hud_count_eq += 1
                    meteo_hud_eq.append(str('[' + txt_col+'EARTHQUAKE' + col_res + '] [' + txt_col + str(fromdate[i]) + col_res + '] [' + txt_col + str(alertlevel[i]) + col_res + '] [' + txt_col + str(country[i]) + col_res + '] [' + txt_col + str(severity[i]) + col_res +  '] [' + txt_col + str(durationinweek[i]) + col_res + '] [' + txt_col + str(population[i]) + col_res + ']'))

            elif str(eventtype[i]) == 'TC':
                if hud_count_tc in hud_event_type_limit:
                    hud_count_tc += 1
                    meteo_hud_tc.append(str('[' + txt_col + 'TROPICAL CYCLONE' + col_res + '] [' + txt_col + str(fromdate[i]) + col_res + '] [' + txt_col + str(alertlevel[i]) + col_res + '] [' + txt_col + str(country[i]) + col_res + '] [' + txt_col + str(eventname[i]) + col_res + '] [' + txt_col + str(durationinweek[i]) + col_res + '] [' + txt_col + str(population[i]) + col_res + ']'))

            elif str(eventtype[i]) == 'FL':
                if hud_count_fl in hud_event_type_limit:
                    hud_count_fl += 1
                    meteo_hud_fl.append(str('[' + txt_col + 'FLOOD' + col_res + '] [' + txt_col + str(fromdate[i]) + col_res + '] [' + txt_col + str(alertlevel[i]) + col_res + '] [' + txt_col + str(country[i]) + col_res + '] [' + txt_col + str(severity[i]) + col_res + '] [' + txt_col + str(durationinweek[i]) + col_res + '] [' + txt_col + str(population[i]) + col_res + ']'))

            elif str(eventtype[i]) == 'VO':
                if hud_count_vo in hud_event_type_limit:
                    hud_count_vo += 1
                    meteo_hud_vo.append(str('[' + txt_col + 'VOLCANIC' + col_res + '] [' + txt_col + str(fromdate[i]) + col_res + '] [' + txt_col + str(alertlevel[i]) + col_res + '] [' + txt_col + str(country[i]) + col_res + '] [' + txt_col + str(severity[i]) + col_res + '] [' + txt_col + str(durationinweek[i]) + col_res + '] [' + txt_col + str(population[i]) + col_res + ']'))

            elif str(eventtype[i]) == 'DR':
                if hud_count_dr in hud_event_type_limit:
                    hud_count_dr += 1
                    meteo_hud_dr.append(str('[' + txt_col + 'DROUGHT' + col_res + '] [' + txt_col + str(fromdate[i]) + col_res + '] [' + txt_col + str(alertlevel[i]) + col_res + '] [' + txt_col + str(country[i]) + col_res + '] [' + txt_col + str(durationinweek[i]) + col_res + '] [' + txt_col + str(population[i]) + col_res + ']'))

            elif str(eventtype[i]) == 'WF':
                if hud_count_wf in hud_event_type_limit:
                    hud_count_wf += 1
                    meteo_hud_wf.append(str('[' + txt_col + 'WILD FIRE' + col_res + '] [' + txt_col + str(fromdate[i]) + col_res + '] [' + txt_col + str(alertlevel[i]) + col_res + '] [' + txt_col + str(country[i]) + col_res + '] [' + txt_col + str(severity[i]) + col_res + '] [' + txt_col + str(durationinweek[i]) + col_res + '] [' + txt_col + str(population[i]) + col_res + ']'))

            to_file = str('[') + str(title[i]) + '] [' + str(descript[i]) + str((fromdate[i]) + '] [' + str(alertlevel[i]) + '] [' + str(country[i]) + '] [' + str(severity[i]) + '] [' + str(durationinweek[i]) + '] [' + str(population[i]) + ']')

            stored_data = []
            if os.path.exists(dat_file):
                with codecs.open(dat_file, 'r', encoding="UTF-8") as fo:
                    for line in fo:
                        line = line.strip()
                        stored_data.append(line)
                fo.close()
            if to_file not in stored_data:
                with codecs.open(dat_file, 'a', encoding="UTF-8") as fo:
                    fo.write(to_file + '\n')
                fo.close()

            i += 1

    except Exception as e:
        clear_console_line()
        technical_data = str('[Time Now:' + str(datetime.datetime.now()) + ' Issue Time:' + str(tm_stamp) + '] ' + str(e) + '. reattempting in 1 second')
        if debug_mode is False:
            pr_technical_data(technical_data)
        else:
            print(technical_data)
        time.sleep(1)
        meteorological_data()


def nasa_climate():
    global debug_mode, tm_stamp, nasa_climate_data
    try:
        dir_now = './extra_data/'
        distutils.dir_util.mkpath(dir_now)
        dat_file = './extra_data/nasa_climate' + '.txt'

        nasa_climate_data = []
        global_temperature = ''
        carbon_dioxide = ''
        arctic_sea_ice_extent, arctic_sea_ice_extent_units = '', ''
        ice_sheets, ice_sheets_units = '', ''
        sea_level, sea_level_error, sea_level_units = '', '', ''
        ocean_heat_content, ocean_heat_content_error, ocean_heat_content_units = '', '', ''

        url = 'https://climate.nasa.gov/vital-signs/global-temperature/'
        technical_data = str('[' + str(datetime.datetime.now()) + '] -- scanning NASA climate data: ' + url)
        pr_technical_data(technical_data)

        rHead = requests.get(url)
        data = rHead.text
        soup = BeautifulSoup(data, "html.parser")
        for row in soup.find_all():
            # print(row)
            if row is not None:
                var = str(row).strip()
                if var.startswith('<div class="value">'):
                    global_temperature = var
        global_temperature = global_temperature.split()
        global_temperature = '[' + Style.BRIGHT+Fore.GREEN+'Global Temperature: ' + str(global_temperature[2]) + '°C' + Style.RESET_ALL + ']'
        nasa_climate_data.append(global_temperature)

        url = 'https://climate.nasa.gov/vital-signs/carbon-dioxide/'
        technical_data = str('[' + str(datetime.datetime.now()) + '] -- scanning NASA climate data: ' + url)
        pr_technical_data(technical_data)

        rHead = requests.get(url)
        data = rHead.text
        soup = BeautifulSoup(data, "html.parser")
        for row in soup.find_all():
            # print(row)
            if row is not None:
                var = str(row).strip()
                if var.startswith('<div class="value">'):
                    carbon_dioxide = var
        carbon_dioxide = carbon_dioxide.split()
        carbon_dioxide = '[' + Style.BRIGHT+Fore.GREEN+'Carbon Dioxide: ' + str(carbon_dioxide[2]) + 'ppm' + Style.RESET_ALL + ']'
        nasa_climate_data.append(carbon_dioxide)

        url = 'https://climate.nasa.gov/vital-signs/arctic-sea-ice/'
        technical_data = str('[' + str(datetime.datetime.now()) + '] -- scanning NASA climate data: ' + url)
        pr_technical_data(technical_data)

        rHead = requests.get(url)
        data = rHead.text
        soup = BeautifulSoup(data, "html.parser")
        for row in soup.find_all():
            # print(row)
            if row is not None:
                var = str(row).strip()
                if var.startswith('<div class="change_number">'):
                    arctic_sea_ice_extent = var
                if var.startswith('<div class="graph_rate_units">'):
                    arctic_sea_ice_extent_units = var
        arctic_sea_ice_extent = arctic_sea_ice_extent.split()
        arctic_sea_ice_extent_units = arctic_sea_ice_extent_units.split()
        arctic_sea_ice_extent = '[' + Style.BRIGHT+Fore.GREEN+'Arctic Sea Ice: ' + str(arctic_sea_ice_extent[2]) + '% ' + str(arctic_sea_ice_extent_units[3]) + ' ' + str(arctic_sea_ice_extent_units[4]) + Style.RESET_ALL + ']'
        nasa_climate_data.append(arctic_sea_ice_extent)

        url = 'https://climate.nasa.gov/vital-signs/ice-sheets/'
        technical_data = str('[' + str(datetime.datetime.now()) + '] -- scanning NASA climate data: ' + url)
        pr_technical_data(technical_data)

        rHead = requests.get(url)
        data = rHead.text
        soup = BeautifulSoup(data, "html.parser")
        for row in soup.find_all():
            # print(row)
            if row is not None:
                var = str(row).strip()
                if var.startswith('<div class="change_number">'):
                    ice_sheets = var
                if var.startswith('<div class="graph_rate_units">'):
                    ice_sheets_units = var
        ice_sheets = ice_sheets.split()
        ice_sheets_units = ice_sheets_units.split()
        ice_sheets = '[' + Style.BRIGHT+Fore.GREEN+'Ice Sheets: ' + str(ice_sheets[2]) + ' ' + str(ice_sheets_units[2]) + ' ' + str(ice_sheets_units[3]) + ' ' + str(ice_sheets_units[4]) + ' ' + str(ice_sheets_units[5]) + ' ' + str(ice_sheets_units[6]) + Style.RESET_ALL + ']'
        nasa_climate_data.append(ice_sheets)

        url = 'https://climate.nasa.gov/vital-signs/sea-level/'
        technical_data = str('[' + str(datetime.datetime.now()) + '] -- scanning NASA climate data: ' + url)
        pr_technical_data(technical_data)

        rHead = requests.get(url)
        data = rHead.text
        soup = BeautifulSoup(data, "html.parser")
        for row in soup.find_all():
            # print(row)
            if row is not None:
                var = str(row).strip()
                if var.startswith('<div class="value">'):
                    sea_level = var
        sea_level = sea_level.split()
        sea_level = '[' + Style.BRIGHT+Fore.GREEN+'Sea Level: ' + str(sea_level[2]) + str(sea_level[5]) + str(sea_level[6]) + str(sea_level[10]) + Style.RESET_ALL + ']'
        nasa_climate_data.append(sea_level)

        url = 'https://climate.nasa.gov/vital-signs/ocean-heat/'
        technical_data = str('[' + str(datetime.datetime.now()) + '] -- scanning NASA climate data: ' + url)
        pr_technical_data(technical_data)

        rHead = requests.get(url)
        data = rHead.text
        soup = BeautifulSoup(data, "html.parser")
        for row in soup.find_all():
            # print(row)
            if row is not None:
                var = str(row).strip()
                if var.startswith('<div class="value">'):
                    ocean_heat_content = var
        ocean_heat_content = ocean_heat_content.split()
        ocean_heat_content = '[' + Style.BRIGHT+Fore.GREEN+'Ocean Heat Content: ' + str(ocean_heat_content[2]) + str(ocean_heat_content[5]) + str(ocean_heat_content[6]) + str(ocean_heat_content[10]) + Style.RESET_ALL + ']'
        nasa_climate_data.append(ocean_heat_content)

        tm_stamp = str(datetime.datetime.now())
        toFile = '[' + tm_stamp + '] [Global Temperature: ' + global_temperature + '] [Carbon Dioxide: ' + carbon_dioxide + '] [Arctic Sea Ice: ' + arctic_sea_ice_extent + '] [Ice Sheets: ' + ice_sheets + '] [Sea Levels: ' + sea_level + '] [Ocean Heat Content: ' + ocean_heat_content + ']'
        to_file_check = toFile.split('] [')
        tmp_str_to_file = to_file_check[1] + to_file_check[2] + to_file_check[3] + to_file_check[4] + to_file_check[5] + to_file_check[6]

        tmp_str_in_file = ''
        if os.path.exists(dat_file):
            with codecs.open(dat_file, 'r', encoding='utf-8') as fo:
                for line in fo:
                    line = line.strip()
                    line = line.split('] [')
                    tmp_str_in_file = line[1] + line[2] + line[3] + line[4] + line[5] + line[6]

        if tmp_str_in_file != tmp_str_to_file:
            # print('-- nasa climate value updated')
            with codecs.open('./extra_data/nasa_climate.txt', 'a', encoding="UTF-8") as fo:
                fo.write(toFile + '\n')
            fo.close()

    except Exception as e:
        clear_console_line()
        technical_data = str('[Time Now:' + str(datetime.datetime.now()) + ' Issue Time:' + str(tm_stamp) + '] ' + str(e) + '. reattempting in 1 second')
        if debug_mode is False:
            pr_technical_data(technical_data)
        else:
            print(technical_data)
        time.sleep(1)
        nasa_climate()


def funk_0():
    global debug_mode, dir_now, tm_stamp, history
    try:
        clear_console_line()

        title_data = []
        dat_file = dir_now + '/bbc_news-world_' + tm_stamp + '.txt'
        url = 'https://www.bbc.co.uk/news/world'
        technical_data = str('[' + str(datetime.datetime.now()) + '] -- scanning base url: ' + url)
        pr_technical_data(technical_data)

        rHead = requests.get(url)
        data = rHead.text
        soup = BeautifulSoup(data, "html.parser")
        for link in soup.find_all('a'):
            href = link.get('href')
            if href is not None and href.startswith('/news/world-'):
                title_data.append(href)

        for _ in title_data:
            url = 'https://www.bbc.co.uk' + _
            if url not in history:
                history.append(url)
                with codecs.open(dat_file, 'a', encoding="UTF-8") as fo:
                    fo.write('\n' + url)
                fo.close()
                clear_console_line()

                technical_data = str('[' + str(datetime.datetime.now()) + '] -- scanning article url: ' + url)
                pr_technical_data(technical_data)

                rHead = requests.get(url)
                data = rHead.text
                soup = BeautifulSoup(data, "html.parser")
                for row in soup.find_all('p'):
                    text = row.get_text()
                    if text is not None:
                        with codecs.open(dat_file, 'a', encoding="UTF-8") as fo:
                            fo.write(text + '\n')
                        fo.close()

    except Exception as e:
        clear_console_line()
        technical_data = str('[Time Now:' + str(datetime.datetime.now()) + ' Issue Time:' + str(tm_stamp) + '] ' + str(e) + '. reattempting in 1 second')
        if debug_mode is False:
            pr_technical_data(technical_data)
        else:
            print(technical_data)
        time.sleep(1)
        funk_0()


def funk_1():
    global debug_mode, dir_now, tm_stamp, history
    try:
        dat_file = dir_now + '/metro_news-world_' + tm_stamp + '.txt'
        date_today = datetime.date.today().strftime('%Y-%m-%d')
        href_data = []
        clear_console_line()
        url = 'https://www.metro.co.uk/news/world'
        technical_data = str('[' + str(datetime.datetime.now()) + '] -- scanning base url: ' + url)
        pr_technical_data(technical_data)
        rHead = requests.get(url)
        data = rHead.text
        soup = BeautifulSoup(data, "html.parser")
        for link in soup.find_all('a'):
            href = link.get('href')
            dt = date_today.replace('-', '/')
            search_str_today = 'https://metro.co.uk/' + dt
            search_str_yesterday = 'https://metro.co.uk/' + dt
            idx = search_str_yesterday.rfind('/')
            search_str_yesterday = search_str_yesterday[:idx]
            if href is not None and href.startswith(search_str_today) or \
                    href is not None and href.startswith(search_str_yesterday):
                if href not in href_data:
                    href_data.append(href)
        i = 0
        for href_datas in href_data:
            url = href_data[i]
            if url not in history:
                history.append(url)
                with codecs.open(dat_file, 'a', encoding="UTF-8") as fo:
                    fo.write('\n' + url)
                fo.close()

                clear_console_line()
                technical_data = str('[' + str(datetime.datetime.now()) + '] -- scanning article url: ' + url)
                pr_technical_data(technical_data)

                rHead = requests.get(url)
                data = rHead.text
                soup = BeautifulSoup(data, "html.parser")
                for row in soup.find_all('p'):
                    text = row.get_text()
                    if text is not None:
                        with codecs.open(dat_file, 'a', encoding="UTF-8") as fo:
                            fo.write(text + '\n')
                        fo.close()
            i += 1
    except Exception as e:
        clear_console_line()
        technical_data = str('[Time Now:' + str(datetime.datetime.now()) + ' Issue Time:' + str(tm_stamp) + '] ' + str(e) + '. reattempting in 1 second')
        if debug_mode is False:
            pr_technical_data(technical_data)
        else:
            print(technical_data)
        time.sleep(1)
        funk_1()


def funk_2():
    global debug_mode, dir_now, tm_stamp, history
    try:
        dat_file = dir_now + '/sky_news-world_' + tm_stamp + '.txt'
        href_data = []
        clear_console_line()
        url = 'https://news.sky.com/world'
        technical_data = str('[' + str(datetime.datetime.now()) + '] -- scanning base url: ' + url)
        pr_technical_data(technical_data)
        rHead = requests.get(url)
        data = rHead.text
        soup = BeautifulSoup(data, "html.parser")
        for link in soup.find_all('a'):
            href = link.get('href')
            if href is not None and href.startswith('/story/'):
                if href not in href_data:
                    href_data.append(href)

        i = 0
        for href_datas in href_data:
            url = 'https://news.sky.com/' + href_data[i]
            if url not in history:
                history.append(url)
                with codecs.open(dat_file, 'a', encoding="UTF-8") as fo:
                    fo.write('\n' + url)
                fo.close()

                clear_console_line()
                technical_data = str('[' + str(datetime.datetime.now()) + '] -- scanning article url: ' + url)
                pr_technical_data(technical_data)

                rHead = requests.get(url)
                data = rHead.text
                soup = BeautifulSoup(data, "html.parser")
                for row in soup.find_all('p'):
                    text = row.get_text()
                    if text is not None:
                        with codecs.open(dat_file, 'a', encoding="UTF-8") as fo:
                            fo.write(text + '\n')
                        fo.close()
            i += 1
    except Exception as e:
        clear_console_line()
        technical_data = str('[Time Now:' + str(datetime.datetime.now()) + ' Issue Time:' + str(tm_stamp) + '] ' + str(e) + '. reattempting in 1 second')
        if debug_mode is False:
            pr_technical_data(technical_data)
        else:
            print(technical_data)
        time.sleep(1)
        funk_2()


def funk_3():
    global debug_mode, dir_now, tm_stamp, history
    try:
        dat_file = dir_now + '/express_news-world_' + tm_stamp + '.txt'
        href_data = []
        clear_console_line()
        url = 'https://www.express.co.uk/news/world'
        technical_data = str('[' + str(datetime.datetime.now()) + '] -- scanning base url: ' + url)
        pr_technical_data(technical_data)
        rHead = requests.get(url)
        data = rHead.text
        soup = BeautifulSoup(data, "html.parser")
        for link in soup.find_all('a'):
            href = link.get('href')
            if href is not None and href.startswith('/news/world') and \
                    href != '/entertainment/world':
                article_url = 'https://www.express.co.uk' + href
                if article_url not in href_data:
                    href_data.append(article_url)
        i = 0
        for href_datas in href_data:
            url = href_data[i]
            if url not in history:
                history.append(url)

                clear_console_line()
                technical_data = str('[' + str(datetime.datetime.now()) + '] -- scanning article url: ' + url)
                pr_technical_data(technical_data)

                rHead = requests.get(url)
                data = rHead.text
                soup = BeautifulSoup(data, "html.parser")
                for row in soup.find_all('p'):
                    text = row.get_text()
                    if text is not None:
                        with codecs.open(dat_file, 'a', encoding="UTF-8") as fo:
                            fo.write(text + '\n')
                        fo.close()
            i += 1
    except Exception as e:
        clear_console_line()
        technical_data = str('[Time Now:' + str(datetime.datetime.now()) + ' Issue Time:' + str(tm_stamp) + '] ' + str(e) + '. reattempting in 1 second')
        if debug_mode is False:
            pr_technical_data(technical_data)
        else:
            print(technical_data)
        time.sleep(1)
        funk_3()


def funk_4():
    global debug_mode, dir_now, tm_stamp, history
    try:
        dat_file = dir_now + '/infowars_world_' + tm_stamp + '.txt'
        title_data = []
        clear_console_line()
        url = 'https://www.infowars.com/category/14/'
        technical_data = str('[' + str(datetime.datetime.now()) + '] -- scanning base url: ' + url)
        pr_technical_data(technical_data)
        rHead = requests.get(url)
        data = rHead.text
        soup = BeautifulSoup(data, "html.parser")
        for link in soup.find_all('a'):
            href = link.get('href')
            if href != None and href.startswith('/posts/'):
                title_data.append(href)
        i = 0
        for title_datas in title_data:
            url = 'https://www.infowars.com' + title_data[i]
            if url not in history:
                history.append(url)
                with codecs.open(dat_file, 'a', encoding="UTF-8") as fo:
                    fo.write('\n' + url)
                fo.close()

                clear_console_line()
                technical_data = str('[' + str(datetime.datetime.now()) + '] -- scanning article url: ' + url)
                pr_technical_data(technical_data)

                rHead = requests.get(url)
                data = rHead.text
                soup = BeautifulSoup(data, "html.parser")
                for row in soup.find_all('p'):
                    text = row.get_text()
                    if text is not None:
                        with codecs.open(dat_file, 'a', encoding="UTF-8") as fo:
                            fo.write(text + '\n')
                        fo.close()
            i += 1
    except Exception as e:
        clear_console_line()
        technical_data = str('[Time Now:' + str(datetime.datetime.now()) + ' Issue Time:' + str(tm_stamp) + '] ' + str(e) + '. reattempting in 1 second')
        if debug_mode is False:
            pr_technical_data(technical_data)
        else:
            print(technical_data)
        time.sleep(1)
        funk_4()


def funk_5():
    global debug_mode, dir_now, tm_stamp, history
    try:
        dat_file = dir_now + '/the_guardian_world_' + tm_stamp + '.txt'
        title_data = []
        filter_year = tm_stamp.split('-')
        clear_console_line()
        url = 'https://www.theguardian.com/world'
        technical_data = str('[' + str(datetime.datetime.now()) + '] -- scanning base url: ' + url)
        pr_technical_data(technical_data)
        rHead = requests.get(url)
        data = rHead.text
        soup = BeautifulSoup(data, "html.parser")
        for link in soup.find_all('a'):
            href = link.get('href')
            if href != None and href.startswith('https://www.theguardian.com/world/' + filter_year[0]):
                title_data.append(href)
        i = 0
        for title_datas in title_data:
            url = title_data[i]
            if url not in history:
                history.append(url)
                with codecs.open(dat_file, 'a', encoding="UTF-8") as fo:
                    fo.write('\n' + url)
                fo.close()

                clear_console_line()
                technical_data = str('[' + str(datetime.datetime.now()) + '] -- scanning article url: ' + url)
                pr_technical_data(technical_data)

                rHead = requests.get(url)
                data = rHead.text
                soup = BeautifulSoup(data, "html.parser")
                for row in soup.find_all('p'):
                    text = row.get_text()
                    if text is not None:
                        with codecs.open(dat_file, 'a', encoding="UTF-8") as fo:
                            fo.write(text + '\n')
                        fo.close()
            i += 1
    except Exception as e:
        clear_console_line()
        technical_data = str('[Time Now:' + str(datetime.datetime.now()) + ' Issue Time:' + str(tm_stamp) + '] ' + str(e) + '. reattempting in 1 second')
        if debug_mode is False:
            pr_technical_data(technical_data)
        else:
            print(technical_data)
        time.sleep(1)
        funk_5()


def funk_6():
    global debug_mode, dir_now, tm_stamp, history
    try:
        dat_file = dir_now + '/daily_mail_world_' + tm_stamp + '.txt'
        title_data = []
        clear_console_line()
        url = 'https://www.dailymail.co.uk/news/worldnews/index.html'
        technical_data = str('[' + str(datetime.datetime.now()) + '] -- scanning base url: ' + url)
        pr_technical_data(technical_data)
        rHead = requests.get(url)
        data = rHead.text
        soup = BeautifulSoup(data, "html.parser")
        for link in soup.find_all('a'):
            href = link.get('href')
            # print(href)
            if href != None and href.startswith('/news/article-'):
                title_data.append(href)
        i = 0
        for title_datas in title_data:
            url = 'https://www.dailymail.co.uk' + title_data[i]
            if url not in history:
                history.append(url)
                with codecs.open(dat_file, 'a', encoding="UTF-8") as fo:
                    fo.write('\n' + url)
                fo.close()

                clear_console_line()
                technical_data = str('[' + str(datetime.datetime.now()) + '] -- scanning article url: ' + url)
                pr_technical_data(technical_data)

                rHead = requests.get(url)
                data = rHead.text
                soup = BeautifulSoup(data, "html.parser")
                for row in soup.find_all('p'):
                    text = row.get_text()
                    if text is not None:
                        with codecs.open(dat_file, 'a', encoding="UTF-8") as fo:
                            fo.write(text + '\n')
                        fo.close()
            i += 1
    except Exception as e:
        clear_console_line()
        technical_data = str('[Time Now:' + str(datetime.datetime.now()) + ' Issue Time:' + str(tm_stamp) + '] ' + str(e) + '. reattempting in 1 second')
        if debug_mode is False:
            pr_technical_data(technical_data)
        else:
            print(technical_data)
        time.sleep(1)
        funk_6()


def funk_7():
    global debug_mode, dir_now, tm_stamp, history
    try:
        dat_file = dir_now + '/rt_world_' + tm_stamp + '.txt'
        title_data = []
        clear_console_line()
        url = 'https://www.rt.com/news/'
        technical_data = str('[' + str(datetime.datetime.now()) + '] -- scanning base url: ' + url)
        pr_technical_data(technical_data)
        rHead = requests.get(url)
        data = rHead.text
        soup = BeautifulSoup(data, "html.parser")
        for link in soup.find_all('a'):
            href = link.get('href')
            if href is not None and href.startswith('/news/') and href != '/news/':
                href = str(href).strip()
                if href not in title_data:
                    title_data.append(href)
        i = 0
        for title_datas in title_data:
            url = 'https://www.rt.com' + title_data[i]
            if url not in history:
                history.append(url)
                with codecs.open(dat_file, 'a', encoding="UTF-8") as fo:
                    fo.write('\n' + url)
                fo.close()

                clear_console_line()
                technical_data = str('[' + str(datetime.datetime.now()) + '] -- scanning article url: ' + url)
                pr_technical_data(technical_data)

                rHead = requests.get(url)
                data = rHead.text
                soup = BeautifulSoup(data, "html.parser")
                for row in soup.find_all('p'):
                    text = row.get_text()
                    if text is not None:
                        with codecs.open(dat_file, 'a', encoding="UTF-8") as fo:
                            fo.write(text + '\n')
                        fo.close()
            i += 1
    except Exception as e:
        clear_console_line()
        technical_data = str('[Time Now:' + str(datetime.datetime.now()) + ' Issue Time:' + str(tm_stamp) + '] ' + str(e) + '. reattempting in 1 second')
        if debug_mode is False:
            pr_technical_data(technical_data)
        else:
            print(technical_data)
        time.sleep(1)
        funk_7()


def funk_8():
    global debug_mode, dir_now, tm_stamp, history
    try:
        dat_file = dir_now + '/nytimes_world_' + tm_stamp + '.txt'
        title_data = []

        clear_console_line()
        url = 'https://www.nytimes.com/section/world'
        technical_data = str('[' + str(datetime.datetime.now()) + '] -- scanning base url: ' + url)
        pr_technical_data(technical_data)

        rHead = requests.get(url)
        data = rHead.text
        soup = BeautifulSoup(data, "html.parser")
        for link in soup.find_all('a'):
            href = link.get('href')
            href_scan_world = href.split('/')
            if len(href_scan_world) > 5:
                href_scan_world = href_scan_world[4]
                if 'world' in href_scan_world:
                    href = str(href).strip()
                    if href not in title_data:
                        title_data.append(href)
        i = 0
        for title_datas in title_data:
            url = 'https://www.nytimes.com' + title_data[i]
            if url not in history:
                history.append(url)
                with codecs.open(dat_file, 'a', encoding="UTF-8") as fo:
                    fo.write('\n' + url)
                fo.close()

                clear_console_line()
                technical_data = str('[' + str(datetime.datetime.now()) + '] -- scanning article url: ' + url)
                pr_technical_data(technical_data)

                rHead = requests.get(url)
                data = rHead.text
                soup = BeautifulSoup(data, "html.parser")
                for row in soup.find_all('p'):
                    text = row.get_text()
                    if text is not None:
                        with codecs.open(dat_file, 'a', encoding="UTF-8") as fo:
                            fo.write(text + '\n')
                        fo.close()
            i += 1
    except Exception as e:
        clear_console_line()
        technical_data = str('[Time Now:' + str(datetime.datetime.now()) + ' Issue Time:' + str(tm_stamp) + '] ' + str(e) + '. reattempting in 1 second')
        if debug_mode is False:
            pr_technical_data(technical_data)
        else:
            print(technical_data)
        time.sleep(1)
        funk_8()


def funk_9():
    global debug_mode, dir_now, tm_stamp, history
    try:
        dat_file = dir_now + '/lifenews_world_' + tm_stamp + '.txt'
        title_data = []

        clear_console_line()
        url = 'https://www.lifenews.com/category/international/'
        technical_data = str('[' + str(datetime.datetime.now()) + '] -- scanning base url: ' + url)
        pr_technical_data(technical_data)

        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        result = requests.get(url, headers=headers)
        x = result.content.decode().split('\n')
        for _ in x:
            _ = _.strip()
            if _.startswith('<a href="https://www.lifenews.com/'):
                _ = str(_).replace('<a href="', '')
                idx = _.rfind('"')
                _ = _[:idx]
                if _.endswith('/'):
                    if _ not in title_data:
                        title_data.append(_)
        i = 0
        for title_datas in title_data:
            url = title_data[i]
            if url not in history:
                history.append(url)
                with codecs.open(dat_file, 'a', encoding="UTF-8") as fo:
                    fo.write('\n' + url)
                fo.close()

                clear_console_line()
                technical_data = str('[' + str(datetime.datetime.now()) + '] -- scanning article url: ' + url)
                pr_technical_data(technical_data)

                headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
                result = requests.get(url, headers=headers)
                x = result.content.decode().split('\n')
                for _ in x:
                    _ = _.strip()
                    if _.startswith('<p>') and not _.startswith('<p><'):
                        _ = _.replace('<p>', '')
                        with codecs.open(dat_file, 'a', encoding="UTF-8") as fo:
                            fo.write(_ + '\n')
                        fo.close()
            i += 1
    except Exception as e:
        clear_console_line()
        technical_data = str('[Time Now:' + str(datetime.datetime.now()) + ' Issue Time:' + str(tm_stamp) + '] ' + str(e) + '. reattempting in 1 second')
        if debug_mode is False:
            pr_technical_data(technical_data)
        else:
            print(technical_data)
        time.sleep(1)
        funk_9()


def invalid_input():
    print('-- invalid input: reinitializing')
    time.sleep(1)
    initialize()


def initialize():
    global debug_mode, tm_stamp

    first_run = True

    while True:
        clear_console()
        print(Style.BRIGHT + Back.RED + str(' ' * char_limit) + Style.RESET_ALL)
        print('')
        print('[1] Run')
        print('[2] Run (debug mode))')
        print('[Q] Quit')
        user_input = input('\nSelect: ')

        # Run Once
        if user_input == '1':
            debug_mode = False
        elif user_input == '2':
            debug_mode = True

        # Quit & Invalid Input
        elif user_input == 'q' or user_input == 'Q':
            clear_console()
            break
        else:
            invalid_input()

        clear_console()
        print(Style.BRIGHT + Back.RED + str(' ' * char_limit) + Style.RESET_ALL)
        print('')
        print('Set time interval in seconds between loops.')
        print('[Q] Quit')
        user_input_2 = input('\nEnter: ')

        if user_input_2.isdigit():
            user_input_2 = int(user_input_2)
            clear_console()
            print(Style.BRIGHT + Back.RED + str(' ' * char_limit) + Style.RESET_ALL)
            print('')
            while True:
                tm_stamp = datetime.datetime.now()
                make_dirs()
                meteorological_data()
                funk_extras()
                nasa_climate()
                sol_news()

                clear_console_line()
                technical_data = str('[' + str(datetime.datetime.now()) + '] -- sleeping:' + str(user_input_2) + ' seconds')
                pr_technical_data(technical_data)

                if first_run is True:
                    first_run = False

                else:
                    time.sleep(user_input_2)

        # Quit & Invalid Input
        elif user_input_2 == 'q' or user_input_2 == 'Q':
            clear_console()
            break
        else:
            invalid_input()


initialize()
