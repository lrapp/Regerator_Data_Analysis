import tkinter as tk
from tkinter import ttk
import pandas as pd
import os
import matplotlib 
matplotlib.use("TkAgg")

from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib import dates 
#ave_for_fit,print_ave_value,calc_Q,int_Q,

from tkinter_file_def import (popupmsg,
                              update_plot,
                              clear_states,
                              getxlim,
                              find_closest_cycle,
                              BV_range_update,
                              create_subplot,
                              remove_subplot,
                              create_averaged_plot,
                              save_averaged_data,
                              add_steady)


#root="C:\\Users\\Logan\\OneDrive - UW-Madison\\Research\\Data Store\\Data\\"

#root="C:\\Users\\Logan\\Documents\\1-Logan\\SEL Research\\Data\\"

root=os.getcwd()+"\\Data\\"

file_list=os.listdir(root)

LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)

style.use("ggplot")

f=Figure()
a=f.add_subplot(111)
a.xaxis_date()
hfmt=dates.DateFormatter('%H:%M:%S')
a.xaxis.set_major_formatter(hfmt)


file_list=str()
file_list_full=os.listdir(root)
for i in range(0,len(file_list_full)):
    file_list=file_list+file_list_full[i]+'\n\n'
    

#%%
class Graph(tk.Frame):
        def __init__(self,parent,controller,file_date):
            self.ex_date=file_date
            tk.Frame.__init__(self,parent)
            import os       
    
            LARGE_FONT = ("Verdana", 12)
            
#            root="C:\\Users\\Logan\\OneDrive - UW-Madison\\Research\\Data Store\\Data\\"
#           root_file_list=os.listdir(root)   
#           file_date="7_20_17_2"
            frame0=tk.Frame(self)                                                   #Define Top Frame
            
            warning_var=tk.StringVar()                                              #Define Warning string variable
                             
                                    
                                    
            label = tk.Label(frame0,text=file_date, font=LARGE_FONT)                #Define Page Label 
            label.grid(row=0,column=1,padx=10)
            
            button1 = ttk.Button(frame0,text="Back to Home",                        #Define Home Button
                                command=lambda: controller.show_frame(StartPage))
            button1.grid(row=0,column=2)                                            #Place Home Button
    
            warning_msg=tk.Label(frame0,textvariable=warning_var)
            warning_msg.grid(row=0,column=3)
            
            frame0.pack()                                                           #Place Top Frame
                  
    
         
            
            folder=root+file_date
            file_list=os.listdir(folder)
                
            if "df_full_cols.h5" in file_list:
                df=pd.read_hdf(folder+"\\df_full_cols.h5",'table')
                warning_var.set("df_full_cols h5 found")
            elif "df_full_cols.csv" in file_list:
                df=pd.read_csv(folder+"\\df_full_cols.csv",index_col=[0],parse_dates=True)
                warning_var.set("df_full_cols found")
            else:
                df=pd.read_csv(folder+"\\df.csv",index_col=[0],parse_dates=True)
                warning_var.set("df_full_cols does not exist for this date")
                    
                    
    
            BV=pd.read_csv(folder+"\\BV.csv",index_col=[0],parse_dates=True)
            cycle_time=(BV.index[1]-BV.index[0]).total_seconds()
                    
            file_list4=os.listdir(folder)
            
            
#            start_date=LR_date()
            
            year_var=tk.StringVar()
            month_var=tk.StringVar()
            day_var=tk.StringVar()
            hour_var=tk.StringVar()
            min_var=tk.StringVar()
            sec_var=tk.StringVar()
            
#            end_date=LR_date()
            
            end_hour_var=tk.StringVar()
            end_min_var=tk.StringVar()
            end_sec_var=tk.StringVar()
            
            
            steady_year_var=tk.StringVar()
            steady_month_var=tk.StringVar()
            steady_day_var=tk.StringVar()
            steady_hour_var=tk.StringVar()
            steady_min_var=tk.StringVar()
            steady_sec_var=tk.StringVar()
            
            steady_end_hour_var=tk.StringVar()
            steady_end_min_var=tk.StringVar()
            steady_end_sec_var=tk.StringVar()
            
            
            year="20"+file_date.split('_')[2]
            month=file_date.split('_')[0]
            if len(month)==1:
                month="0"+month
            day=file_date.split('_')[1]
            
            
            
            col_list=df.columns.tolist()
    #        col_list=df_full_cols.columns.tolist()        
            DP_list=col_list[0:5]
            P_list=col_list[7:14]
            T_list=col_list[22:62]+col_list[14:24]
            m_list=col_list[5:7]+col_list[76:78]
            h_list=col_list[62:76]
            mu_list=col_list[78:92]
            rho_list=col_list[92:106]
            
    
            var_DP=[]
            var_P=[]
            var_T=[]
            var_m=[]
            var_h=[]
            var_mu=[]
            var_rho=[]
            
            var2_DP=[]
            var2_P=[]
            var2_T=[]
            var2_m=[]
            var2_h=[]
            var2_mu=[]
            var2_rho=[]
            
            sep_col_list=[DP_list,P_list,T_list,m_list,h_list,mu_list,rho_list]
            
            var_list=[var_DP,var_P,var_T,var_m,var_h,var_mu,var_rho]
            
            var_list2=[var2_DP,var2_P,var2_T,var2_m,var2_h,var2_mu,var2_rho]
            
            full_list=DP_list+P_list+T_list+m_list+h_list+mu_list+rho_list
    
            
            for j in range(0,len(sep_col_list)):
                for i in range(0,len(sep_col_list[j])):
                    var_list[j].append(tk.IntVar())
            
            for j in range(0,len(sep_col_list)):
                for i in range(0,len(sep_col_list[j])):
                    var_list[j][i].set(0)
                    
                    
            for j in range(0,len(sep_col_list)):
                for i in range(0,len(sep_col_list[j])):
                    var_list2[j].append(tk.IntVar())
            
            
            for j in range(0,len(sep_col_list)):
                for i in range(0,len(sep_col_list[j])):
                    var_list2[j][i].set(0)            
                    
         
    
    
            
            note=ttk.Notebook(self)  
            frame_holder=tk.Frame(self)
            frame1=tk.Frame(frame_holder)
            frame2=tk.Frame(frame_holder)
            
            frame_holder_pg2=tk.Frame(self)
            frame1_pg2=tk.Frame(frame_holder_pg2)
            frame2_pg2=tk.Frame(frame_holder_pg2)
            
    
    
    
            col_index=0
            col_index_mult=0
            for j in range(0,len(sep_col_list)):
                for i in range(0,len(sep_col_list[j])):
                    rb=ttk.Checkbutton(frame1,text=sep_col_list[j][i],variable=var_list[j][i])
                    if i % 5 == 0:
                        col_index_mult=col_index_mult+1
                       
                    rb.grid(row=i%5,column=col_index_mult,padx=10)  
                    col_index=col_index+1 
                col_index_mult=col_index_mult+5
    
            full_var_list=var_DP+var_P+var_T+var_m+var_h+var_mu+var_rho       
                                
    
            radiobutton1_text=["All Data","Steady State"]  
            steady_all_radiobutt=[]
            if "df_full_cols_steady.csv" in file_list4:
                df_steady=pd.read_csv(folder+"\\df_full_cols_steady.csv",index_col=[0],parse_dates=True)
                for i in range(0,2):
                    steady_all_radiobutt.append(tk.IntVar())
                    radiobutton1=ttk.Checkbutton(frame2,text=radiobutton1_text[i],variable=steady_all_radiobutt[i])
                    radiobutton1.grid(row=0,column=3+i,pady=5)
            else:
                steady_all_radiobutt.append(tk.IntVar())
                df_steady=df
                radiobutton1=ttk.Radiobutton(frame2,text=["All Data"],variable=steady_all_radiobutt[0])
                radiobutton1.grid(row=0,pady=5)
    
#            button2=ttk.Button(frame2,text="print active checkbox",
#                               command=lambda:popupmsg(get_states(auto_axis_var)))
#            button2.grid(row=0,column=1,padx=10)
    
            button3=ttk.Button(frame2,text="Update Plot",
                               command=lambda:update_plot(1,f,full_var_list,full_list,a,df,df_steady,self,canvas,steady_all_radiobutt,year_var,month_var,day_var,hour_var,min_var,sec_var,end_hour_var,end_min_var,end_sec_var,auto_axis_var,plot_var))
                               

            button3.grid(row=0,column=2,pady=5)
            
            button4=ttk.Button(frame2,text="Clear Selection",command=lambda:clear_states(var_list))
            button4.grid(row=0,column=0)
    
    
            frame1.pack()
            frame2.pack()
            
            
            col_index=0
            col_index_mult=0
            for j in range(0,len(sep_col_list)):
                for i in range(0,len(sep_col_list[j])):
                    rb=ttk.Checkbutton(frame1_pg2,text=sep_col_list[j][i],variable=var_list2[j][i])
                    if i % 5 == 0:
                        col_index_mult=col_index_mult+1
                       
                    rb.grid(row=i%5,column=col_index_mult,padx=10)  
                    col_index=col_index+1 
                col_index_mult=col_index_mult+5
            
    
            full_var_list2=var2_DP+var2_P+var2_T+var2_m+var2_h+var2_mu+var2_rho 
    
            radiobutton1_text=["All Data","Steady State"]  
            steady_all_radiobutt_pg2=[]
            if "df_full_cols_steady.csv" in file_list4:
                df_steady=pd.read_csv(folder+"\\df_full_cols_steady.csv",index_col=[0],parse_dates=True)
    
                for i in range(0,2):
                    steady_all_radiobutt_pg2.append(tk.IntVar())
                    radiobutton1_pg2=ttk.Checkbutton(frame2_pg2,text=radiobutton1_text[i],variable=steady_all_radiobutt_pg2[i])
                    radiobutton1_pg2.grid(row=0,column=3+i,pady=5)
            else:
                steady_all_radiobutt_pg2.append(tk.IntVar())
                radiobutton1=ttk.Radiobutton(frame2_pg2,text=["All Data"],variable=steady_all_radiobutt_pg2[0])
                radiobutton1.grid(row=0,pady=5)

            button3_pg2=ttk.Button(frame2_pg2,text="Update Plot",
                               command=lambda:update_plot(2,f,full_var_list2,full_list,a,df,df_steady,self,canvas,steady_all_radiobutt,year_var,month_var,day_var,hour_var,min_var,sec_var,end_hour_var,end_min_var,end_sec_var,auto_axis_var,plot_var))
                               

            button3_pg2.grid(row=0,column=1,pady=5)
            
            button4_pg2=ttk.Button(frame2_pg2,text="Clear Selection",command=lambda:clear_states(var_list2))
            button4_pg2.grid(row=0,column=0)
            
            frame1_pg2.pack()
            frame2_pg2.pack()
            
            note.add(frame_holder,text='one')
            note.add(frame_holder_pg2,text='two')
            note.pack()
    
    
            frame3=tk.Frame(self)
            auto_axis_text=["Set X Start","Set X End"]
            auto_axis_var=[tk.IntVar(),tk.IntVar()]
            for i in range(0,len(auto_axis_text)):
                plot_axis_checkbutton=ttk.Checkbutton(frame3,text=auto_axis_text[i],variable=auto_axis_var[i])
                plot_axis_checkbutton.grid(row=0,column=i+13,rowspan=2)
                
    
            year_var.set(year)
            month_var.set(month)
            day_var.set(day)
            
            
#            start_date.year.set(year)
#            start_date.month.set(month)
#            start_date.day.set(day)
#                        
#            end_date.year.set(year)
#            end_date.month.set(month)
#            end_date.day.set(day)
#            
            steady_year_var.set(year)
            steady_month_var.set(month)
            steady_day_var.set(day)
            
            x_start=tk.Entry(frame3,width=4,state='readonly',textvariable=year_var)
            x_start.grid(row=0,column=0)
            
            x_start=tk.Entry(frame3,width=2,state='readonly',textvariable=month_var)            

            x_start.grid(row=0,column=1)
            
            x_start=tk.Entry(frame3,width=2,state='readonly',textvariable=day_var)       
            x_start.grid(row=0,column=2)
            
            x_start=tk.Entry(frame3,width=2,state='normal',textvariable=hour_var)
       
            x_start.grid(row=0,column=3)
            
            x_start=tk.Entry(frame3,width=2,state='normal',textvariable=min_var)
            x_start.grid(row=0,column=4)
            
            x_start=tk.Entry(frame3,width=2,state='normal',textvariable=sec_var)        
            x_start.grid(row=0,column=5)
            
            x_space=tk.Label(frame3,width=5)
            x_space.grid(row=1,column=6)
                    
            x_start=tk.Entry(frame3,width=4,state='readonly',textvariable=year_var)
            x_start.grid(row=0,column=7)
            
            x_start=tk.Entry(frame3,width=2,state='readonly',textvariable=month_var)      
            x_start.grid(row=0,column=8)
            
            x_start=tk.Entry(frame3,width=2,state='readonly',textvariable=day_var)          
            x_start.grid(row=0,column=9)
            
            x_start=tk.Entry(frame3,width=2,state='normal',textvariable=end_hour_var)
            x_start.grid(row=0,column=10)
            
            x_start=tk.Entry(frame3,width=2,state='normal',textvariable=end_min_var)
            x_start.grid(row=0,column=11)
            
            x_start=tk.Entry(frame3,width=2,state='normal',textvariable=end_sec_var)         
            x_start.grid(row=0,column=12)
            
            get_x_lim=ttk.Button(frame3,text="Get X Lim",command=lambda:getxlim(f,year_var,month_var,day_var,hour_var,min_var,sec_var,end_hour_var,end_min_var,end_sec_var))
            get_x_lim.grid(row=0,column=15)
            
            find_closest=ttk.Button(frame3,text="Find Closest",command=lambda:find_closest_cycle(f,year_var,month_var,day_var,hour_var,min_var,sec_var,end_hour_var,end_min_var,end_sec_var,BV,BV_start_var,BV_end_var))
            find_closest.grid(row=0,column=16)
    
    
    #        date_start_list=["Year","Month","Day","Hour","Min","Sec"]
    #        for i in range(0,len(date_start_list)):
    #            if i < 3:
    #                x_start=ttk.Entry(frame3,width=5,state='disabled')
    #                x_start.grid(row=0,column=i)
                
            BV_start_var=tk.StringVar()
            BV_start_label=tk.Entry(frame3,textvariable=BV_start_var,justify='center')
            BV_start_label.grid(row=1,column=0,columnspan=6)
            
            BV_end_var=tk.StringVar()
            BV_end_label=tk.Entry(frame3,textvariable=BV_end_var,justify='center')
            BV_end_label.grid(row=1,column=7,columnspan=6)
            
            BV_button=ttk.Button(frame3,text='Update limits to BV range',command=lambda:BV_range_update(f,BV,BV_start_var,BV_end_var,auto_axis_var,hour_var,min_var,sec_var,end_hour_var,end_min_var,end_sec_var))
            

            BV_button.grid(row=1,column=15,columnspan=2)
            
            plot_var=tk.IntVar()
            
            radio_butt=ttk.Radiobutton(frame3,value=0,text='Line',variable=plot_var)
            radio_butt.grid(row=1,column=17)
            radio_butt=ttk.Radiobutton(frame3,value=1,text='Circle',variable=plot_var)
            radio_butt.grid(row=1,column=18)
            radio_butt=ttk.Radiobutton(frame3,value=2,text='Both',variable=plot_var)
            radio_butt.grid(row=1,column=19)
            
#            test_butt=ttk.Button(frame3,text="check plot var",command=lambda:popupmsg(plot_var.get()))
#            test_butt.grid(row=1,column=20)
            
            add_subplot_butt=ttk.Button(frame3,text="create subplot",command=lambda:create_subplot(1,f,full_var_list,full_list,a,df,df_steady,self,canvas,steady_all_radiobutt,year_var,month_var,day_var,hour_var,min_var,sec_var,end_hour_var,end_min_var,end_sec_var,auto_axis_var,plot_var))
            add_subplot_butt.grid(row=0,column=20,padx=20)
            
            remove_subplot_butt=ttk.Button(frame3,text="Remove subplot",command=lambda:remove_subplot(1,f,full_var_list,full_list,a,df,df_steady,self,canvas,steady_all_radiobutt,year_var,month_var,day_var,hour_var,min_var,sec_var,end_hour_var,end_min_var,end_sec_var,auto_axis_var,plot_var))
            remove_subplot_butt.grid(row=1,column=20)
            
            x_space2=tk.Label(frame3,width=5)
            x_space2.grid(row=0,column=22,rowspan=2)
            
            add_averaged=ttk.Button(frame3,text="Add Averaged Data Plot",command=lambda:create_averaged_plot(2,f,full_var_list,full_list,a,df,df_steady,self,canvas,steady_all_radiobutt,year_var,month_var,day_var,hour_var,min_var,sec_var,end_hour_var,end_min_var,end_sec_var,auto_axis_var,plot_var,
                                                                                                             steady_year_var,steady_month_var,steady_day_var,steady_hour_var,steady_min_var,steady_sec_var,steady_end_hour_var,steady_end_min_var,steady_end_sec_var,
                                                                                                              cycle_start_var,cycle_end_var,
                                                                                                              ST1_ave_var,ST3_ave_var,
                                                                                                              cycle_time))
            add_averaged.grid(row=0,column=23,rowspan=1)
    
            save_averaged=ttk.Button(frame3,text="save averaged data",command=lambda:save_averaged_data(df,cycle_start_var,cycle_end_var))
            save_averaged.grid(row=1,column=23)
    
            steady_hour_var.set(df.index[0].hour)
            steady_min_var.set(df.index[0].minute)
            steady_sec_var.set(df.index[0].second)
            
            steady_end_hour_var.set(df.index[-1].hour)
            steady_end_min_var.set(df.index[-1].minute)
            steady_end_sec_var.set(df.index[-1].second)
            
            steady_x_start=tk.Entry(frame3,width=4,state='readonly',textvariable=steady_year_var)
            steady_x_start.grid(row=0,column=24)
            
            steady_x_start=tk.Entry(frame3,width=2,state='readonly',textvariable=steady_month_var)
            steady_x_start.grid(row=0,column=25)
            
            steady_x_start=tk.Entry(frame3,width=2,state='readonly',textvariable=steady_day_var)
            steady_x_start.grid(row=0,column=26)
            
            steady_x_start=tk.Entry(frame3,width=2,state='normal',textvariable=steady_hour_var)
            steady_x_start.grid(row=0,column=27)
            
            steady_x_start=tk.Entry(frame3,width=2,state='normal',textvariable=steady_min_var)
            steady_x_start.grid(row=0,column=28)
            
            steady_x_start=tk.Entry(frame3,width=2,state='normal',textvariable=steady_sec_var)
            steady_x_start.grid(row=0,column=29)
            
            steady_x_space=tk.Label(frame3,width=5)
            steady_x_space.grid(row=1,column=30)
                    
            steady_x_start=tk.Entry(frame3,width=4,state='readonly',textvariable=steady_year_var)
            steady_x_start.grid(row=0,column=31)
            
            steady_x_start=tk.Entry(frame3,width=2,state='readonly',textvariable=steady_month_var)
            steady_x_start.grid(row=0,column=32)
            
            steady_x_start=tk.Entry(frame3,width=2,state='readonly',textvariable=steady_day_var)
            steady_x_start.grid(row=0,column=33)
            
            steady_x_start=tk.Entry(frame3,width=2,state='normal',textvariable=steady_end_hour_var)
            steady_x_start.grid(row=0,column=34)
            
            steady_x_start=tk.Entry(frame3,width=2,state='normal',textvariable=steady_end_min_var)
            steady_x_start.grid(row=0,column=35)
            
            steady_x_start=tk.Entry(frame3,width=2,state='normal',textvariable=steady_end_sec_var)
            steady_x_start.grid(row=0,column=36)
            
            cycle_start_var=tk.StringVar()
            cycle_start=tk.Entry(frame3,textvariable=cycle_start_var,justify='center')
            cycle_start.grid(row=1,column=24,columnspan=6)
            
            cycle_end_var=tk.StringVar()
            cycle_end=tk.Entry(frame3,textvariable=cycle_end_var,justify='center')
            cycle_end.grid(row=1,column=31,columnspan=6)
            
            get_x_lim2=ttk.Button(frame3,text="Get X Lim",command=lambda:getxlim(f,steady_year_var,steady_month_var,steady_day_var,steady_hour_var,steady_min_var,steady_sec_var,steady_end_hour_var,steady_end_min_var,steady_end_sec_var))
            get_x_lim2.grid(row=0,column=37)
            
            find_closest2=ttk.Button(frame3,text="Find Closest",command=lambda:find_closest_cycle(f,steady_year_var,steady_month_var,steady_day_var,steady_hour_var,steady_min_var,steady_sec_var,steady_end_hour_var,steady_end_min_var,steady_end_sec_var,BV,cycle_start_var,cycle_end_var))
            find_closest2.grid(row=0,column=38)
            
            BV_button2=ttk.Button(frame3,text='Update limits to BV range',command=lambda:BV_range_update(f,BV,cycle_start_var,cycle_end_var,auto_axis_var,steady_hour_var,steady_min_var,steady_sec_var,steady_end_hour_var,steady_end_min_var,steady_end_sec_var))
            BV_button2.grid(row=1,column=37,columnspan=2)
            
            add_steady_to_plot=ttk.Button(frame3,text='Add Steady State to Plot',command=lambda: add_steady(1,f,df,full_var_list,full_list,a,df_steady,self,canvas,steady_all_radiobutt,year_var,month_var,day_var,hour_var,min_var,sec_var,end_hour_var,end_min_var,end_sec_var,auto_axis_var,plot_var,
                  steady_year_var,steady_month_var,steady_day_var,steady_hour_var,steady_min_var,steady_sec_var,steady_end_hour_var,steady_end_min_var,steady_end_sec_var))
          
            add_steady_to_plot.grid(row=0,column=39)
            
            frame3.pack(anchor='w')
            
            frame4=tk.Frame(self)
#            
            ST1_ave_var=tk.StringVar()
            
            ST1_ave_var.set(str(0.0))
            
            ST1_label_label=tk.Label(frame4,text="ST1_ave=")
            ST1_label_label.grid(row=0,column=0)
            ST1_ave_label=tk.Label(frame4,textvariable=ST1_ave_var)
            ST1_ave_label.grid(row=0,column=1)
            
            ST3_ave_var=tk.StringVar()
            
            ST3_ave_var.set(str(0.0))
            
            ST3_label_label=tk.Label(frame4,text="ST3_ave=")
            ST3_label_label.grid(row=0,column=2)
            ST3_ave_label=tk.Label(frame4,textvariable=ST3_ave_var)
            ST3_ave_label.grid(row=0,column=3)
          
            frame4.pack(anchor='e')
    
            canvas = FigureCanvasTkAgg(f,self)
            canvas.show()
            canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=True)
            
            toolbar = NavigationToolbar2TkAgg(canvas,self)
            toolbar.update()
            canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand=True)   
#%%
class StartPage(tk.Frame):
    def __init__(self,parent,controller,Graph_list):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self,text="Start Page", font=LARGE_FONT,justify=tk.CENTER,width=10)
        label.pack(pady=10,padx=10)

        f=tk.Frame(self)
                       
        tk_button_list=[]
        for i in range(0,len(Graph_list)):
             tk_button_list.append(ttk.Button(f,text=Graph_list[i].ex_date,
                        command=lambda i=i: controller.show_frame(Graph_list[i])))
             tk_button_list[i].grid(row=i+1,column=0)

        f.pack()
        
        
#%%            
class exPlotapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)   
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both",expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        menubar = tk.Menu(container)
        filemenu=tk.Menu(menubar,tearoff=0)
        filemenu.add_command(label="Save Settings",command = lambda: popupmsg("Not Supported yet"))
        filemenu.add_separator()
        filemenu.add_command(label="Exit",command=quit)
        menubar.add_cascade(label="File",menu=filemenu)

        tk.Tk.config(self,menu=menubar)
        
        self.frames = {}

        date_list=["4_26_17",
                   "5_15_17_1",
                   "5_15_17_2",
                   "5_18_17",
                   "6_7_17",
                   "6_10_17",
                   "7_14_17",
                   "7_20_17",
                   "7_20_17_2",
                   "7_28_17_1",
                   "7_28_17_2",
                   "8_1_17",
				   "8_16_17"]
        
        
                   
        Graph_list=[]
        for i in range(0,len(date_list)):
            Graph_list.append(Graph(container,self,date_list[i]))
            self.frames[Graph_list[i]]=Graph_list[i]
            Graph_list[i].grid(row=0,column=0,sticky="nsew")

        
        frame=StartPage(container,self,Graph_list)
        self.frames[StartPage]=frame
        frame.grid(row=0,column=0,sticky="nsew")

        
        self.show_frame(StartPage)
        
    def show_frame(self, cont):
        frame =self.frames[cont]
        frame.tkraise()
          
       

        
app = exPlotapp()
app.geometry("1280x720")
app.mainloop()
        