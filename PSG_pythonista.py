import ui
import console
import get_time
import get_data
import calc
import matplotlib.pyplot as plt
import pylab
import matplotlib.dates as mdates
import pylab
from io import BytesIO

def graph_single_dictionary(dictionary1):
    plt.clf()
    empty = []
    x_list = []
    y_list = []
    for key in sorted(dictionary1.keys()):
        x_list.append(key)
        y_list.append(dictionary1[key])

    n_1 = len(x_list)
    x = range(n_1)

    plt.style.use('dark_background')
    plt.axis('off')
    plt.rcParams['lines.linewidth'] = 6
    plt.plot(x,y_list, color='red')
    plt.ylim(ymin=0)

    b = BytesIO()
    plt.savefig(b, bbox_inches='tight', transparent='True')
    return b

def graph_dual_dictionary(dictionary1,dictionary2):
    plt.clf()
    empty = []
    x1_list = []
    y1_list = []

    x2_list = []
    y2_list = []

    for key in sorted(dictionary1.keys()):
        x1_list.append(key)
        y1_list.append(dictionary1[key])
    len_x1 = len(x1_list)
    x1 = range(len_x1)

    for key in sorted(dictionary2.keys()):
        x2_list.append(key)
        y2_list.append(dictionary2[key])
    len_x2 = len(x2_list)
    x2 = range(len_x2)

    if len_x1 > len_x2:
        x3 = range(len_x1)
    if len_x1 < len_x2:
        x3 = range(len_x2)

    plt.style.use('dark_background')
    plt.axis('off')
    plt.rcParams['lines.linewidth'] = 6
    plt.plot(x1,y1_list, color='red')
    plt.plot(x2,y2_list, color='blue')
    plt.ylim(ymin=0)

    b = BytesIO()
    plt.savefig(b, bbox_inches='tight', transparent='True')
    return b

def get_information():
    global button_3_status
    button_3_status = 7
    global dataset
    dataset = get_data.my_activities()

def main():
    global button_2_status
    button_2_status = "All"
    my_dataset = dataset.copy()
    global dict_time_dist
    global dict_time_pace
    dict_time_dist,dict_time_pace = calc.filter(my_dataset)

    running_week_dict = calc.var_calc_loop_single(get_time.running_week(0),my_dataset)
    this_week_dict = calc.var_calc_loop_single(get_time.LM(0),my_dataset)
    last_week_dict = calc.var_calc_loop_double(get_time.LM(1),get_time.LS(0),my_dataset)
    this_month_dict = calc.var_calc_loop_single(get_time.FOM(0),my_dataset)
    last_month_dict = calc.var_calc_loop_double(get_time.FOM(1),get_time.LOM(1),my_dataset)
    YTD_dict = calc.var_calc_loop_single(get_time.FOY(),my_dataset)

    label1= v['label1']
    label1.text = this_week_dict['miles']

    label2= v['label2']
    label2.text = this_week_dict['pace']

    label3= v['label3']
    label3.text = this_week_dict['count']

    label4= v['label4']
    label4.text = this_month_dict['miles']

    label5= v['label5']
    label5.text = this_month_dict['pace']

    label6= v['label6']
    label6.text = this_month_dict['count']

    label7= v['label7']
    label7.text = running_week_dict['miles']

    label8= v['label8']
    label8.text = running_week_dict['pace']

    label9= v['label9']
    label9.text = running_week_dict['count']

    label11= v['label11']
    label11.text = last_week_dict['miles']

    label12= v['label12']
    label12.text = last_week_dict['pace']

    label13= v['label13']
    label13.text = last_week_dict['count']

    label14= v['label14']
    label14.text = last_month_dict['miles']

    label15= v['label15']
    label15.text = last_month_dict['pace']

    label16= v['label16']
    label16.text = last_month_dict['count']

    label17= v['label17']
    label17.text = YTD_dict['miles']

    label18= v['label18']
    label18.text = YTD_dict['pace']

    label19= v['label19']
    label19.text = YTD_dict['count']

    label81= v['label81']
    label81.text = this_week_dict['date']

    label82= v['label82']
    label82.text = this_month_dict['date']

    label82= v['label83']
    label82.text = running_week_dict['date']

    label83= v['label84']
    label83.text = last_week_dict['date']

    label84= v['label85']
    label84.text = last_month_dict['date']

    label85= v['label86']
    label85.text = YTD_dict['date']

def main_solo():
    global button_2_status
    button_2_status = "Solo"

    my_dataset = dataset.copy()
    global dict_time_dist
    global dict_time_pace
    dict_time_dist,dict_time_pace = calc.solo_filter(my_dataset)

    running_week_dict = calc.var_calc_loop_single(get_time.running_week(0),my_dataset)
    this_week_dict = calc.var_calc_loop_single(get_time.LM(0),my_dataset)
    last_week_dict = calc.var_calc_loop_double(get_time.LM(1),get_time.LS(0),my_dataset)
    this_month_dict = calc.var_calc_loop_single(get_time.FOM(0),my_dataset)
    last_month_dict = calc.var_calc_loop_double(get_time.FOM(1),get_time.LOM(1),my_dataset)
    YTD_dict = calc.var_calc_loop_single(get_time.FOY(),my_dataset)

    label1= v['label1']
    label1.text = this_week_dict['solo_miles']

    label2= v['label2']
    label2.text = this_week_dict['solo_pace']

    label3= v['label3']
    label3.text = this_week_dict['solo_count']

    label4= v['label4']
    label4.text = this_month_dict['solo_miles']

    label5= v['label5']
    label5.text = this_month_dict['solo_pace']

    label6= v['label6']
    label6.text = this_month_dict['solo_count']

    label7= v['label7']
    label7.text = running_week_dict['solo_miles']

    label8= v['label8']
    label8.text = running_week_dict['solo_pace']

    label9= v['label9']
    label9.text = running_week_dict['solo_count']

    label11= v['label11']
    label11.text = last_week_dict['solo_miles']

    label12= v['label12']
    label12.text = last_week_dict['solo_pace']

    label13= v['label13']
    label13.text = last_week_dict['solo_count']

    label14= v['label14']
    label14.text = last_month_dict['solo_miles']

    label15= v['label15']
    label15.text = last_month_dict['solo_pace']

    label16= v['label16']
    label16.text = last_month_dict['solo_count']

    label17= v['label17']
    label17.text = YTD_dict['solo_miles']

    label18= v['label18']
    label18.text = YTD_dict['solo_pace']

    label19= v['label19']
    label19.text = YTD_dict['solo_count']

    label81= v['label81']
    label81.text = this_week_dict['date']

    label82= v['label82']
    label82.text = this_month_dict['date']

    label82= v['label83']
    label82.text = running_week_dict['date']

    label83= v['label84']
    label83.text = last_week_dict['date']

    label84= v['label85']
    label84.text = last_month_dict['date']

    label85= v['label86']
    label85.text = YTD_dict['date']

def main_partner():
    global button_2_status
    button_2_status = "Partner"

    my_dataset = dataset.copy()
    global dict_time_dist
    global dict_time_pace
    dict_time_dist,dict_time_pace = calc.partner_filter(my_dataset)

    running_week_dict = calc.var_calc_loop_single(get_time.running_week(0),my_dataset)
    this_week_dict = calc.var_calc_loop_single(get_time.LM(0),my_dataset)
    last_week_dict = calc.var_calc_loop_double(get_time.LM(1),get_time.LS(0),my_dataset)
    this_month_dict = calc.var_calc_loop_single(get_time.FOM(0),my_dataset)
    last_month_dict = calc.var_calc_loop_double(get_time.FOM(1),get_time.LOM(1),my_dataset)
    YTD_dict = calc.var_calc_loop_single(get_time.FOY(),my_dataset)

    label1= v['label1']
    label1.text = this_week_dict['partner_miles']

    label2= v['label2']
    label2.text = this_week_dict['partner_pace']

    label3= v['label3']
    label3.text = this_week_dict['partner_count']

    label4= v['label4']
    label4.text = this_month_dict['partner_miles']

    label5= v['label5']
    label5.text = this_month_dict['partner_pace']

    label6= v['label6']
    label6.text = this_month_dict['partner_count']

    label7= v['label7']
    label7.text = running_week_dict['partner_miles']

    label8= v['label8']
    label8.text = running_week_dict['partner_pace']

    label9= v['label9']
    label9.text = running_week_dict['partner_count']

    label11= v['label11']
    label11.text = last_week_dict['partner_miles']

    label12= v['label12']
    label12.text = last_week_dict['partner_pace']

    label13= v['label13']
    label13.text = last_week_dict['partner_count']

    label14= v['label14']
    label14.text = last_month_dict['partner_miles']

    label15= v['label15']
    label15.text = last_month_dict['partner_pace']

    label16= v['label16']
    label16.text = last_month_dict['partner_count']

    label17= v['label17']
    label17.text = YTD_dict['partner_miles']

    label18= v['label18']
    label18.text = YTD_dict['partner_pace']

    label19= v['label19']
    label19.text = YTD_dict['partner_count']

    label81= v['label81']
    label81.text = this_week_dict['date']

    label82= v['label82']
    label82.text = this_month_dict['date']

    label82= v['label83']
    label82.text = running_week_dict['date']

    label83= v['label84']
    label83.text = last_week_dict['date']

    label84= v['label85']
    label84.text = last_month_dict['date']

    label85= v['label86']
    label85.text = YTD_dict['date']

def button_action_2(sender):

    if button2.selected_index == 0:
        main()

    if button2.selected_index == 1:
        main_solo()

    elif button2.selected_index == 2:
        main_partner()

def button_action_3(sender):
    global button_3_status
    if button3.selected_index == 0:
        button_3_status = 7
    if button3.selected_index == 1:
        button_3_status = 8
    elif button3.selected_index == 2:
        button_3_status = 90


def button_action_1(sender):

    if button1.selected_index == 0:
        #red is 90, blue is 91 - current month is red past month is blue
        v['label90'].text = "This Week"
        v['label91'].text = "Last Week"
        v['label92'].text = button_2_status
        b = graph_dual_dictionary(calc.running_totals_single(dict_time_dist,button_3_status,get_time.LM(0)),calc.running_totals_double(dict_time_dist,button_3_status,get_time.LM(2),get_time.LS(1)))
        v['imageview1'].image = ui.Image.from_data(b.getvalue())

    if button1.selected_index == 1:
        v['label90'].text ='This Month'
        v['label91'].text ='Last Month'
        v['label92'].text = button_2_status
        b = graph_dual_dictionary(calc.running_totals_single(dict_time_dist,button_3_status,get_time.FOM(0)),calc.running_totals_double(dict_time_dist,button_3_status,get_time.FOM(1),get_time.LOM(1)))
        v['imageview1'].image = ui.Image.from_data(b.getvalue())

    elif button1.selected_index == 2:
        v['label90'].text ='2017 To Date'
        v['label91'].text =''
        v['label92'].text = button_2_status
        b = graph_single_dictionary(calc.running_totals_single(dict_time_dist,button_3_status,get_time.FOY()))
        v['imageview1'].image = ui.Image.from_data(b.getvalue())

get_information()

# starts gui
v = ui.load_view()
v.background_color = "black"

button1 = v['segmentedcontrol1']
button1.action = button_action_1
button2 = v['segmentedcontrol2']
button2.action = button_action_2
button3 = v['segmentedcontrol3']
button3.action = button_action_3

v.present(style='sheet', hide_title_bar=True)

main()
