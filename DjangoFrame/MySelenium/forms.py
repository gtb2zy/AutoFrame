from django import forms
class LoginForm(forms.Form):
	username=forms.CharField(widget=forms.TextInput)
	password=forms.CharField(widget=forms.PasswordInput)
class AddForm(forms.Form):
	day_before_choices=(('',''),('1','1'),('7','7'),('10','10'))
	operate_name_choices=(('',''),('click','click'),('input','input'),('open_window','open_window'),('select','select'),('deselect','deselect'),('switch_window','switch_window'),('tap_key','tap_key'),('clip','clip'),('press_key','press_key'),('release_key','release_key'),('move','move'),('quit','quit'))
	element1_name_choices=(('',''),('id','id'),('index','index'),('value','value'),('visible_text','visible_text'),('link_text','link_text'),('tab_key','tab_key'),('enter_key','enter_key'),('control_key','control_key'),('v','v'),(r'D:\all_list\table.xlsx',r'D:\all_list\table.xls'))
	element1_value_choices=(('',''),('UserID','UserID'),('UserPass','UserPass'),('ButtonSubmit','ButtonSubmit'),('NeControl_TypeList','NeControl_TypeList'),('btnSelAll','btnSelAll'),('TimeControl1_DdlbReportType','TimeControl1_DdlbReportType'),('TimeControl1_LbYear','TimeControl1_LbYear'),('TimeControl1_LbMonth','TimeControl1_LbMonth'),('TimeControl1_LbDay','TimeControl1_LbDay'),('TimeControl1_LbHour','TimeControl1_LbHour'),('TimeControl1_ButtonAdd','TimeControl1_ButtonAdd'),('CreateExcelBtn','CreateExcelBtn'),('（如不能下载请点这里）','（如不能下载请点这里）'),('1','1'),('3','3'),('4','4'))
	element2_name_choices=(('',''),('id','id'),('index','index'),('value','value'),('visible_text','visible_text'),('0','0'),('1','1'))
	element2_value_choices=(('',''),('1','1'),('MSC','MSC'),('str((datetime.now()+timedelta(days=-int(day_before))).year)+" 年"','str((datetime.now()+timedelta(days=-int(day_before))).year)+" 年"'),('str((datetime.now()+timedelta(days=-int(day_before))).month)+" 月"','str((datetime.now()+timedelta(days=-int(day_before))).month)+" 月"'),('str((datetime.now()+timedelta(days=-int(day_before))).day)+" 日"','str((datetime.now()+timedelta(days=-int(day_before))).day)+" 日"'),('str(datetime.now().day)+" 日"','str(datetime.now().day)+" 日"'),('str(datetime.now().hour)+" 时"','str(datetime.now().day)+" 时"'))
	wait_time_choices=(('0','0'),('1','1'),('2','2'),('3','3'),('5','5'),('10','10'),('20','20'))
	path_format_choices=(('',''),('0','0'))
	name_format_choices=(('',''),('0','0'))
	name=forms.CharField(label='表名',widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
	day_before=forms.ChoiceField(label='距今天数',widget=forms.Select(attrs={'class':'form-control'}),required=False,choices=day_before_choices)
	operate_name1=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=operate_name_choices,required=False)
	element1_name1=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_name_choices,required=False)
	element1_value1=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_value_choices,required=False)
	element2_name1=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_name_choices,required=False)
	element2_value1=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_value_choices,required=False)
	extra1=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
	wait_time1=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=wait_time_choices,required=False)
	operate_name2=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=operate_name_choices,required=False)
	element1_name2=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_name_choices,required=False)
	element1_value2=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_value_choices,required=False)
	element2_name2=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_name_choices,required=False)
	element2_value2=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_value_choices,required=False)
	extra2=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
	wait_time2=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=wait_time_choices,required=False)
	operate_name3=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=operate_name_choices,required=False)
	element1_name3=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_name_choices,required=False)
	element1_value3=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_value_choices,required=False)
	element2_name3=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_name_choices,required=False)
	element2_value3=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_value_choices,required=False)
	extra3=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
	wait_time3=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=wait_time_choices,required=False)
	operate_name4=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=operate_name_choices,required=False)	
	element1_name4=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_name_choices,required=False)
	element1_value4=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_value_choices,required=False)
	element2_name4=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_name_choices,required=False)
	element2_value4=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_value_choices,required=False)
	extra4=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
	wait_time4=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=wait_time_choices,required=False)
	operate_name5=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=operate_name_choices,required=False)	
	element1_name5=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_name_choices,required=False)
	element1_value5=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_value_choices,required=False)
	element2_name5=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_name_choices,required=False)
	element2_value5=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_value_choices,required=False)
	extra5=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
	wait_time5=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=wait_time_choices,required=False)
	operate_name6=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=operate_name_choices,required=False)	
	element1_name6=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_name_choices,required=False)
	element1_value6=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_value_choices,required=False)
	element2_name6=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_name_choices,required=False)
	element2_value6=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_value_choices,required=False)
	extra6=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
	wait_time6=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=wait_time_choices,required=False)
	operate_name7=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=operate_name_choices,required=False)	
	element1_name7=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_name_choices,required=False)
	element1_value7=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_value_choices,required=False)
	element2_name7=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_name_choices,required=False)
	element2_value7=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_value_choices,required=False)
	extra7=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
	wait_time7=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=wait_time_choices,required=False)
	operate_name8=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=operate_name_choices,required=False)	
	element1_name8=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_name_choices,required=False)
	element1_value8=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_value_choices,required=False)
	element2_name8=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_name_choices,required=False)
	element2_value8=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_value_choices,required=False)
	extra8=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
	wait_time8=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=wait_time_choices,required=False)
	operate_name9=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=operate_name_choices,required=False)	
	element1_name9=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_name_choices,required=False)
	element1_value9=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_value_choices,required=False)
	element2_name9=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_name_choices,required=False)
	element2_value9=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_value_choices,required=False)
	extra9=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
	wait_time9=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=wait_time_choices,required=False)
	operate_name10=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=operate_name_choices,required=False)	
	element1_name10=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_name_choices,required=False)
	element1_value10=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_value_choices,required=False)
	element2_name10=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_name_choices,required=False)
	element2_value10=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_value_choices,required=False)
	extra10=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
	wait_time10=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=wait_time_choices,required=False)
	operate_name11=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=operate_name_choices,required=False)	
	element1_name11=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_name_choices,required=False)
	element1_value11=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_value_choices,required=False)
	element2_name11=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_name_choices,required=False)
	element2_value11=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_value_choices,required=False)
	extra11=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
	wait_time11=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=wait_time_choices,required=False)
	operate_name12=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=operate_name_choices,required=False)	
	element1_name12=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_name_choices,required=False)
	element1_value12=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_value_choices,required=False)
	element2_name12=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_name_choices,required=False)
	element2_value12=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_value_choices,required=False)
	extra12=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
	wait_time12=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=wait_time_choices,required=False)
	operate_name13=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=operate_name_choices,required=False)	
	element1_name13=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_name_choices,required=False)
	element1_value13=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_value_choices,required=False)
	element2_name13=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_name_choices,required=False)
	element2_value13=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_value_choices,required=False)
	extra13=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
	wait_time13=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=wait_time_choices,required=False)
	operate_name14=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=operate_name_choices,required=False)	
	element1_name14=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_name_choices,required=False)
	element1_value14=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_value_choices,required=False)
	element2_name14=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_name_choices,required=False)
	element2_value14=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_value_choices,required=False)
	extra14=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
	wait_time14=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=wait_time_choices,required=False)
	operate_name15=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=operate_name_choices,required=False)	
	element1_name15=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_name_choices,required=False)
	element1_value15=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_value_choices,required=False)
	element2_name15=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_name_choices,required=False)
	element2_value15=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_value_choices,required=False)
	extra15=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
	wait_time15=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=wait_time_choices,required=False)
	operate_name16=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=operate_name_choices,required=False)	
	element1_name16=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_name_choices,required=False)
	element1_value16=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_value_choices,required=False)
	element2_name16=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_name_choices,required=False)
	element2_value16=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_value_choices,required=False)
	extra16=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
	wait_time16=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=wait_time_choices,required=False)
	operate_name17=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=operate_name_choices,required=False)	
	element1_name17=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_name_choices,required=False)
	element1_value17=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_value_choices,required=False)
	element2_name17=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_name_choices,required=False)
	element2_value17=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_value_choices,required=False)
	extra17=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
	wait_time17=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=wait_time_choices,required=False)
	operate_name18=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=operate_name_choices,required=False)	
	element1_name18=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_name_choices,required=False)
	element1_value18=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_value_choices,required=False)
	element2_name18=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_name_choices,required=False)
	element2_value18=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_value_choices,required=False)
	extra18=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
	wait_time18=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=wait_time_choices,required=False)
	operate_name19=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=operate_name_choices,required=False)	
	element1_name19=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_name_choices,required=False)
	element1_value19=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_value_choices,required=False)
	element2_name19=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_name_choices,required=False)
	element2_value19=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_value_choices,required=False)
	extra19=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
	wait_time19=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=wait_time_choices,required=False)
	operate_name20=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=operate_name_choices,required=False)	
	element1_name20=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_name_choices,required=False)
	element1_value20=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_value_choices,required=False)
	element2_name20=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_name_choices,required=False)
	element2_value20=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_value_choices,required=False)
	extra20=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
	wait_time20=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=wait_time_choices,required=False)
	operate_name21=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=operate_name_choices,required=False)	
	element1_name21=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_name_choices,required=False)
	element1_value21=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_value_choices,required=False)
	element2_name21=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_name_choices,required=False)
	element2_value21=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_value_choices,required=False)
	extra21=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
	wait_time21=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=wait_time_choices,required=False)
	operate_name22=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=operate_name_choices,required=False)	
	element1_name22=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_name_choices,required=False)
	element1_value22=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_value_choices,required=False)
	element2_name22=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_name_choices,required=False)
	element2_value22=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_value_choices,required=False)
	extra22=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
	wait_time22=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=wait_time_choices,required=False)
	operate_name23=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=operate_name_choices,required=False)	
	element1_name23=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_name_choices,required=False)
	element1_value23=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_value_choices,required=False)
	element2_name23=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_name_choices,required=False)
	element2_value23=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_value_choices,required=False)
	extra23=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
	wait_time23=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=wait_time_choices,required=False)
	operate_name24=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=operate_name_choices,required=False)	
	element1_name24=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_name_choices,required=False)
	element1_value24=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_value_choices,required=False)
	element2_name24=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_name_choices,required=False)
	element2_value24=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_value_choices,required=False)
	extra24=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
	wait_time24=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=wait_time_choices,required=False)
	operate_name25=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=operate_name_choices,required=False)	
	element1_name25=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_name_choices,required=False)
	element1_value25=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_value_choices,required=False)
	element2_name25=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_name_choices,required=False)
	element2_value25=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_value_choices,required=False)
	extra25=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
	wait_time25=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=wait_time_choices,required=False)
	operate_name26=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=operate_name_choices,required=False)	
	element1_name26=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_name_choices,required=False)
	element1_value26=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_value_choices,required=False)
	element2_name26=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_name_choices,required=False)
	element2_value26=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_value_choices,required=False)
	extra26=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
	wait_time26=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=wait_time_choices,required=False)
	operate_name27=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=operate_name_choices,required=False)	
	element1_name27=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_name_choices,required=False)
	element1_value27=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_value_choices,required=False)
	element2_name27=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_name_choices,required=False)
	element2_value27=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_value_choices,required=False)
	extra27=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
	wait_time27=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=wait_time_choices,required=False)
	operate_name28=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=operate_name_choices,required=False)	
	element1_name28=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_name_choices,required=False)
	element1_value28=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_value_choices,required=False)
	element2_name28=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_name_choices,required=False)
	element2_value28=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_value_choices,required=False)
	extra28=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
	wait_time28=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=wait_time_choices,required=False)
	operate_name29=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=operate_name_choices,required=False)	
	element1_name29=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_name_choices,required=False)
	element1_value29=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_value_choices,required=False)
	element2_name29=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_name_choices,required=False)
	element2_value29=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_value_choices,required=False)
	extra29=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
	wait_time29=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=wait_time_choices,required=False)
	operate_name30=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=operate_name_choices,required=False)	
	element1_name30=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_name_choices,required=False)
	element1_value30=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element1_value_choices,required=False)
	element2_name30=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_name_choices,required=False)
	element2_value30=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=element2_value_choices,required=False)
	extra30=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
	wait_time30=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=wait_time_choices,required=False)
