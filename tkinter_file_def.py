import numpy as np
import pandas as pd
import FIT_HXR
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from scipy import integrate
from matplotlib import dates 
import matplotlib 
import datetime

def ave_for_fit(full,cycle_time,Q_C1_ave,Q_H1_ave,Q_C2_ave,Q_H2_ave,Q_C1_std,Q_H1_std,Q_C2_std,Q_H2_std,half_cycle_time_ave):
    target=1
    target_code=1
    n_hxrs=25
    
    dp_1=0
#    dp_1=full.loc[full['state']=='STATE1']["DP01_ave"].mean()*6.89475729
    dp_2=dp_1
    
    fluid_1='carbondioxide'
    fluid_2='carbondioxide'
    
    t_in_1_RE2=full.loc[full['state']=='STATE1']["TI12"+"_ave"].mean()              #t_in_1 is T12_ave of state1    
    t_in_2_RE2=full.loc[full['state']=='STATE3']["TI16"+"_ave"].mean()              #t_in_2 is T16_ave of state3
                  
    p_in_1_RE2=full.loc[full['state']=='STATE1']["PT03"+"_ave"].mean()*6.89475729              #p_in_1 is PT03_ave of state1
    p_in_2_RE2=full.loc[full['state']=='STATE3']["PT03"+"_ave"].mean()*6.89475729              #p_in_2 is PT03_ave of state3
    
    m_dot_1_RE2=full.loc[full['state']=='STATE1']["FI01"+"_ave"].mean() 
    m_dot_2_RE2=full.loc[full['state']=='STATE3']["FI01"+"_ave"].mean() 


#    t_in_1_RE1=t_in_1_RE2
#    t_in_2_RE1=t_in_2_RE2
#    
#    p_in_1_RE1=p_in_1_RE2
#    p_in_2_RE1=p_in_2_RE2
#    
#    m_dot_1_RE1=m_dot_1_RE2
#    m_dot_2_RE1=m_dot_2_RE2
    t_in_1_RE1=full.loc[full['state']=='STATE3']["TI07"+"_ave"].mean()              #t_in_1 is T12_ave of state1    
    t_in_2_RE1=full.loc[full['state']=='STATE1']["TI11"+"_ave"].mean()              #t_in_2 is T16_ave of state3
                  
    p_in_1_RE1=full.loc[full['state']=='STATE3']["PT01"+"_ave"].mean()*6.89475729              #p_in_1 is PT03_ave of state1
    p_in_2_RE1=full.loc[full['state']=='STATE1']["PT01"+"_ave"].mean()*6.89475729              #p_in_2 is PT03_ave of state3

    m_dot_1_RE1=full.loc[full['state']=='STATE3']["FI01"+"_ave"].mean() 
    m_dot_2_RE1=full.loc[full['state']=='STATE1']["FI01"+"_ave"].mean() 
    
    [epsilon_target_RE1,dt_min_RE1,ua_RE1,q_dot_RE1,q_dot_max_RE1,t_1_RE1,t_2_RE1]=FIT_HXR.counter_flow(fluid_1,fluid_2,target,target_code,n_hxrs,m_dot_1_RE1,m_dot_2_RE1,t_in_1_RE1,t_in_2_RE1,p_in_1_RE1,p_in_2_RE1,dp_1,dp_2)

    [epsilon_target_RE2,dt_min_RE2,ua_RE2,q_dot_RE2,q_dot_max_RE2,t_1_RE2,t_2_RE2]=FIT_HXR.counter_flow(fluid_1,fluid_2,target,target_code,n_hxrs,m_dot_1_RE2,m_dot_2_RE2,t_in_1_RE2,t_in_2_RE2,p_in_1_RE2,p_in_2_RE2,dp_1,dp_2)
   
    Q_max_RE1=q_dot_max_RE1*cycle_time
    Q_max_RE2=q_dot_max_RE2*cycle_time
    
    Q_dot_C1=Q_C1_ave/half_cycle_time_ave
    
    Q_dot_C2=Q_C2_ave/half_cycle_time_ave
    
    eff_C1=Q_dot_C1/q_dot_max_RE1
    eff_C2=Q_dot_C2/q_dot_max_RE2
    
    
    ave_popupmsg("Q_max_RE1="+str(Q_max_RE1)+"\nQ_dot_max_RE1="+str(q_dot_max_RE1)+"\neff_C1= "+str(eff_C1)+
                 "\nQ_max_RE2="+str(Q_max_RE2)+"\nQ_dot_max_RE2="+str(q_dot_max_RE2)+"\neff_C2= "+str(eff_C2),
                                   dp_1,dp_2,t_in_1_RE1,t_in_2_RE1,p_in_1_RE1,p_in_2_RE1,m_dot_1_RE1,m_dot_2_RE1,
                                   Q_max_RE1,q_dot_max_RE1,t_1_RE1,t_2_RE1,Q_C1_ave,Q_H1_ave,Q_C2_ave,Q_H2_ave,Q_C1_std,
                                   Q_H1_std,Q_C2_std,Q_H2_std,half_cycle_time_ave,eff_C1,eff_C2,Q_max_RE2,
                                   t_in_1_RE2,t_in_2_RE2,p_in_1_RE2,p_in_2_RE2,m_dot_1_RE2,m_dot_2_RE2,q_dot_max_RE2)
#%%     
def print_ave_value(full,full_var_list,full_list,var2,ST1_ave_var,ST3_ave_var):
    var_states=[]
    for i in range(0,len(full_var_list)):
        var_states.append(full_var_list[i].get())             
        
    var2_states=[]
    for i in range(0,len(var2)):
        var2_states.append(var2[i].get())    
        
    plot_vars=[]
    for i in range(0,len(var_states)):
        if var_states[i]==1:
            plot_vars.append(full_list[i])
            
            
    for i in range(0,len(plot_vars)):
        st1_ave_value=round(full.loc[full['state']=='STATE1'][plot_vars[i]+"_ave"].mean(),4)
        st3_ave_value=round(full.loc[full['state']=='STATE3'][plot_vars[i]+"_ave"].mean(),4)
        
    ST1_ave_var.set(str(st1_ave_value))
    ST3_ave_var.set(str(st3_ave_value))
#%%  
def popupmsg(msg):

    NORM_FONT = ("Verdana", 10)
    
    popup=tk.Tk()
        
    popup.wm_title("!")
    label = ttk.Label(popup,text=msg,font=NORM_FONT)
    label.pack(side="top",fill="x",pady=10)
    B1 = ttk.Button(popup,text="Okay",command=popup.destroy)
    B1.pack()   
    popup.mainloop()
#%%

def ave_popupmsg(msg,dp_1,dp_2,t_in_1,t_in_2,p_in_1,p_in_2,m_dot_1,m_dot_2,Q_max,q_dot_max,t_1,t_2,Q_C1_ave,Q_H1_ave,Q_C2_ave,Q_H2_ave,Q_C1_std,Q_H1_std,Q_C2_std,Q_H2_std,half_cycle_time_ave,eff_C1,eff_C2,Q_max_C2,t_in_1_RE2,t_in_2_RE2,p_in_1_RE2,p_in_2_RE2,m_dot_1_RE2,m_dot_2_RE2,q_dot_max_RE2):
    
    NORM_FONT = ("Verdana", 10)
    popup=tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup,text=msg,font=NORM_FONT)
    label.pack(side="top",fill="x",pady=10)
    B1 = ttk.Button(popup,text="Okay",command=popup.destroy)
    B1.pack()
    B2=ttk.Button(popup,text="Save",command=lambda:save_ave_vars(dp_1,dp_2,t_in_1,t_in_2,p_in_1,p_in_2,m_dot_1,m_dot_2,Q_max,q_dot_max,t_1,t_2,Q_C1_ave,Q_H1_ave,Q_C2_ave,Q_H2_ave,Q_C1_std,Q_H1_std,Q_C2_std,Q_H2_std,half_cycle_time_ave,eff_C1,eff_C2,Q_max_C2,t_in_1_RE2,t_in_2_RE2,p_in_1_RE2,p_in_2_RE2,m_dot_1_RE2,m_dot_2_RE2,q_dot_max_RE2))
    B2.pack()
    
    popup.mainloop()
#%%
def save_as():
    import tkinter as tk


    window=tk.Tk()
    window.filename = filedialog.asksaveasfilename()
    save_as_name=window.filename
    window.destroy
    return save_as_name
#%%
def save_ave_vars(dp_1,dp_2,t_in_1,t_in_2,p_in_1,p_in_2,m_dot_1,m_dot_2,Q_max,q_dot_max,t_1,t_2,Q_C1_ave,Q_H1_ave,Q_C2_ave,Q_H2_ave,Q_C1_std,Q_H1_std,Q_C2_std,Q_H2_std,half_cycle_time_ave,eff_C1,eff_C2,Q_max_C2,t_in_1_RE2,t_in_2_RE2,p_in_1_RE2,p_in_2_RE2,m_dot_1_RE2,m_dot_2_RE2,q_dot_max_RE2):
    import io 
    
    name=save_as()
    f=io.open(name,mode='w')
    f.write("dp_1="+str(dp_1))
    f.write("\ndp_2="+str(dp_2))   
    f.write("\nt_in_1_RE1="+str(t_in_1))
    f.write("\nt_in_2_RE1="+str(t_in_2))
    f.write("\np_in_1_RE1="+str(p_in_1))
    f.write("\np_in_2_RE1="+str(p_in_2))
    f.write("\nm_dot_1_RE1="+str(m_dot_1))
    f.write("\nm_dot_2_RE1="+str(m_dot_2))
    
    f.write("\n\nt_in_1_RE2="+str(t_in_1_RE2))
    f.write("\nt_in_2_RE2="+str(t_in_2_RE2))
    f.write("\np_in_1_RE2="+str(p_in_1_RE2))
    f.write("\np_in_2_RE2="+str(p_in_2_RE2))
    f.write("\nm_dot_1_RE2="+str(m_dot_1_RE2))
    f.write("\nm_dot_2_RE2="+str(m_dot_2_RE2))
    
    f.write("\n\nOutputs:")
    f.write("\nQ_max_C1="+str(Q_max))
    f.write("\nQ_max_C2= "+str(Q_max_C2))
    f.write("\nq_dot_max_C1="+str(q_dot_max))   
    f.write("\nq_dot_max_C2="+str(q_dot_max_RE2))

#    f.write("\nt_1="+str(t_1))
#    f.write("\nt_2="+str(t_2))
    f.write("\nExperimental:")
    f.write("\nQ_C1_ave="+str(Q_C1_ave)+"+/-"+str(Q_C1_std))
    f.write("\nQ_H1_ave="+str(Q_H1_ave)+"+/-"+str(Q_H1_std))
    f.write("\nQ_C2_ave="+str(Q_C2_ave)+"+/-"+str(Q_C2_std))
    f.write("\nQ_H2_ave="+str(Q_H2_ave)+"+/-"+str(Q_H2_std))
    f.write("\nhalf cycle time average"+str(half_cycle_time_ave))
    f.write("\n\neff_C1 = "+str(eff_C1))
    f.write("\neff_C2= "+str(eff_C2))
    
    
    f.close() 
#%%
def calc_Q(start,end,df_full_cols):

    
    def integrate_method(self, how='trapz', unit='s'):
        '''Numerically integrate the time series.
    
        @param how: the method to use (trapz by default)
        @return 
    
        Available methods:
         * trapz - trapezoidal
         * cumtrapz - cumulative trapezoidal
         * simps - Simpson's rule
         * romb - Romberger's rule
    
        See http://docs.scipy.org/doc/scipy/reference/integrate.html for the method details.
        or the source code
        https://github.com/scipy/scipy/blob/master/scipy/integrate/quadrature.py
        '''
        available_rules = set(['trapz', 'cumtrapz', 'simps', 'romb'])
        if how in available_rules:
            rule = integrate.__getattribute__(how)
        else:
            print('Unsupported integration rule: %s' % (how))
            print('Expecting one of these sample-based integration rules: %s' % (str(list(available_rules))))
            raise AttributeError
        
        result = rule(self.values, self.index.astype(np.int64) / 10**9)
        #result = rule(self.values)
        return result
    
    pd.TimeSeries.integrate = integrate_method
    
    
    Q_C1=[]
    Q_H1=[]
    Q_C2=[]
    Q_H2=[]
    Q_H2_ST2a=[]
    Q_C1_ST2a=[]
    Q_H2_ST2b=[]
    Q_C1_ST2b=[]    
    
    half_cycle_time=[]
    for i in range(start,end):
        if df_full_cols.loc[df_full_cols['cycle_num']==i]['state'][0] =='STATE1':
            df_i=df_full_cols.loc[df_full_cols['cycle_num']==i]
            half_cycle_time.append((df_i.index[-1]-df_i.index[0]).total_seconds())
            Q16=(integrate.trapz(df_i['h16']*df_i['FI01'],df_i.index.astype(np.int64)/10**9))
            Q12=(integrate.trapz(df_i['h12']*df_i['FI01'],df_i.index.astype(np.int64)/10**9))
            Q11=(integrate.trapz(df_i['h11']*df_i['FI01'],df_i.index.astype(np.int64)/10**9))
            Q07=(integrate.trapz(df_i['h07']*df_i['FI01'],df_i.index.astype(np.int64)/10**9))
            
            Q_H2.append(Q16-Q12)
            Q_C1.append(Q11-Q07)
        if df_full_cols.loc[df_full_cols['cycle_num']==i]['state'][0] =='STATE3':
            df_i=df_full_cols.loc[df_full_cols['cycle_num']==i]
            Q16=(integrate.trapz(df_i['h16']*df_i['FI01'],df_i.index.astype(np.int64)/10**9))
            Q12=(integrate.trapz(df_i['h12']*df_i['FI01'],df_i.index.astype(np.int64)/10**9))
            Q11=(integrate.trapz(df_i['h11']*df_i['FI01'],df_i.index.astype(np.int64)/10**9))
            Q07=(integrate.trapz(df_i['h07']*df_i['FI01'],df_i.index.astype(np.int64)/10**9))
            
            Q_H1.append(Q11-Q07)
            Q_C2.append(Q16-Q12)
            
        if df_full_cols.loc[df_full_cols['cycle_num']==i]['state'][0] =='STATE2a':  
            df_i=df_full_cols.loc[df_full_cols['cycle_num']==i]
#            half_cycle_time.append((df_i.index[-1]-df_i.index[0]).total_seconds())
            Q16=(integrate.trapz(df_i['h16']*df_i['FI01'],df_i.index.astype(np.int64)/10**9))
            Q12=(integrate.trapz(df_i['h12']*df_i['FI01'],df_i.index.astype(np.int64)/10**9))
            Q11=(integrate.trapz(df_i['h11']*df_i['FI01'],df_i.index.astype(np.int64)/10**9))
            Q07=(integrate.trapz(df_i['h07']*df_i['FI01'],df_i.index.astype(np.int64)/10**9))
            
            Q_H2_ST2a.append(Q16-Q12)
            Q_C1_ST2a.append(Q11-Q07)
            
        if df_full_cols.loc[df_full_cols['cycle_num']==i]['state'][0] =='STATE2b':  
            df_i=df_full_cols.loc[df_full_cols['cycle_num']==i]
#            half_cycle_time.append((df_i.index[-1]-df_i.index[0]).total_seconds())
            Q16=(integrate.trapz(df_i['h16']*df_i['FI01'],df_i.index.astype(np.int64)/10**9))
            Q12=(integrate.trapz(df_i['h12']*df_i['FI01'],df_i.index.astype(np.int64)/10**9))
            Q11=(integrate.trapz(df_i['h11']*df_i['FI01'],df_i.index.astype(np.int64)/10**9))
            Q07=(integrate.trapz(df_i['h07']*df_i['FI01'],df_i.index.astype(np.int64)/10**9))
            
            Q_H2_ST2b.append(Q16-Q12)
            Q_C1_ST2b.append(Q11-Q07)
            
            
            
            
           
    Q_C1_ave=np.mean(Q_C1)
    Q_H1_ave=np.mean(Q_H1)
    Q_C2_ave=np.mean(Q_C2)
    Q_H2_ave=np.mean(Q_H2)
    half_cycle_time_ave=np.mean(half_cycle_time)
    Q_C1_std=np.std(Q_C1)
    Q_H1_std=np.std(Q_H1)
    Q_C2_std=np.std(Q_C2)
    Q_H2_std=np.std(Q_H2)
    

    
    return [Q_C1_ave,Q_H1_ave,Q_C2_ave,Q_H2_ave,Q_C1_std,Q_H1_std,Q_C2_std,Q_H2_std,half_cycle_time_ave]
#%%
def int_Q():
    from scipy import integrate
    import pandas as pd
    import numpy as np
    def integrate_method(self, how='trapz', unit='s'):
        '''Numerically integrate the time series.
    
        @param how: the method to use (trapz by default)
        @return 
    
        Available methods:
         * trapz - trapezoidal
         * cumtrapz - cumulative trapezoidal
         * simps - Simpson's rule
         * romb - Romberger's rule
    
        See http://docs.scipy.org/doc/scipy/reference/integrate.html for the method details.
        or the source code
        https://github.com/scipy/scipy/blob/master/scipy/integrate/quadrature.py
        '''

        available_rules = set(['trapz', 'cumtrapz', 'simps', 'romb'])
        if how in available_rules:
            rule = integrate.__getattribute__(how)
        else:
            print('Unsupported integration rule: %s' % (how))
            print('Expecting one of these sample-based integration rules: %s' % (str(list(available_rules))))
            raise AttributeError
        
        result = rule(self.values, self.index.astype(np.int64) / 10**9)
        #result = rule(self.values)
        return result

    pd.TimeSeries.integrate = integrate_method
#%%
def add_steady(update_plot_num,f,df,full_var_list,full_list,a,df_steady,self,canvas,steady_all_radiobutt,year_var,month_var,day_var,hour_var,min_var,sec_var,end_hour_var,end_min_var,end_sec_var,auto_axis_var,plot_var,
               steady_year_var,steady_month_var,steady_day_var,steady_hour_var,steady_min_var,steady_sec_var,steady_end_hour_var,steady_end_min_var,steady_end_sec_var):
    import datetime
    a.clear()
    
    a=f.get_children()[update_plot_num]
    update_plot(update_plot_num,f,full_var_list,full_list,a,df,df_steady,self,canvas,steady_all_radiobutt,year_var,month_var,day_var,hour_var,min_var,sec_var,end_hour_var,end_min_var,end_sec_var,auto_axis_var,plot_var)

    var_states=[]
    for i in range(0,len(full_var_list)):
        var_states.append(full_var_list[i].get()) 
    
    plot_vars=[]
    for i in range(0,len(var_states)):
        if var_states[i]==1:
            plot_vars.append(full_list[i])
    
    steady_start=datetime.datetime(int(steady_year_var.get()),int(steady_month_var.get()),int(steady_day_var.get()),int(steady_hour_var.get()),int(steady_min_var.get()),int(steady_sec_var.get()))
    steady_end=datetime.datetime(int(steady_year_var.get()),int(steady_month_var.get()),int(steady_day_var.get()),int(steady_end_hour_var.get()),int(steady_end_min_var.get()),int(steady_end_sec_var.get()))
    
    df_s=df[df.index>=steady_start]
    df_s=df_s[df_s.index<=steady_end]
    leg_loc=2
    for i in range(0,len(plot_vars)):
        if plot_var.get()==0:
            a.plot(df_s.index,df_s[plot_vars[i]],label=plot_vars[i])
            a.legend(bbox_to_anchor=(1,1), loc=leg_loc,fontsize=10)
        if plot_var.get()==1:
            a.plot(df_s.index,df_s[plot_vars[i]],'o',label=plot_vars[i],markersize=4)
            a.legend(bbox_to_anchor=(1,1), loc=leg_loc,fontsize=10)
        if plot_var.get()==2:
            a.plot(df_s.index,df_s[plot_vars[i]],'-o',label=plot_vars[i],markersize=4)
            a.legend(bbox_to_anchor=(1,1), loc=leg_loc,fontsize=10)
    
    canvas.show()
#%%
def average_cycle(start,end,df_full_cols):

    st1_list=[]
    st2a_list=[]
    st2b_list=[]
    st2c_list=[]
    st3_list=[]
    st4a_list=[]
    st4b_list=[]
    st4c_list=[]
    
    ave_list=[st1_list,st2a_list,st2b_list,st2c_list,st3_list,st4a_list,st4b_list,st4c_list]
    
    for i in range(start,end):
        num=len(df_full_cols.loc[df_full_cols['cycle_num']==i])
        if df_full_cols.loc[df_full_cols['cycle_num']==i]['state'][0] =='STATE1':
            cycle_index_num=np.linspace(0,num-1,num,dtype=int)
            df_i=df_full_cols.loc[df_full_cols['cycle_num']==i]
            df_i.insert(1,'cycle index',cycle_index_num)
            time_d=[]
            for j in range(0,num):
                time_d.append((df_i.index[j]-df_i.index[0]).total_seconds())
            df_i.insert(0,'rel_time',time_d)
            st1_list.append(df_i)
        if df_full_cols.loc[df_full_cols['cycle_num']==i]['state'][0] =='STATE2a':
            cycle_index_num=np.linspace(0,num-1,num,dtype=int)
            df_i=df_full_cols.loc[df_full_cols['cycle_num']==i]
            df_i.insert(1,'cycle index',cycle_index_num)
            time_d=[]
            for j in range(0,num):
                time_d.append((df_i.index[j]-df_i.index[0]).total_seconds())
            df_i.insert(0,'rel_time',time_d)            
            st2a_list.append(df_i)
        if df_full_cols.loc[df_full_cols['cycle_num']==i]['state'][0] =='STATE2b':
            cycle_index_num=np.linspace(0,num-1,num,dtype=int)
            df_i=df_full_cols.loc[df_full_cols['cycle_num']==i]
            df_i.insert(1,'cycle index',cycle_index_num)
            time_d=[]
            for j in range(0,num):
                time_d.append((df_i.index[j]-df_i.index[0]).total_seconds())
            df_i.insert(0,'rel_time',time_d)         
            st2b_list.append(df_i)
        if df_full_cols.loc[df_full_cols['cycle_num']==i]['state'][0] =='STATE2c':
            cycle_index_num=np.linspace(0,num-1,num,dtype=int)
            df_i=df_full_cols.loc[df_full_cols['cycle_num']==i]
            df_i.insert(1,'cycle index',cycle_index_num)
            time_d=[]
            for j in range(0,num):
                time_d.append((df_i.index[j]-df_i.index[0]).total_seconds())
            df_i.insert(0,'rel_time',time_d)         
            st2c_list.append(df_i)
        if df_full_cols.loc[df_full_cols['cycle_num']==i]['state'][0] =='STATE3':
            cycle_index_num=np.linspace(0,num-1,num,dtype=int)
            df_i=df_full_cols.loc[df_full_cols['cycle_num']==i]
            df_i.insert(1,'cycle index',cycle_index_num)
            time_d=[]
            for j in range(0,num):
                time_d.append((df_i.index[j]-df_i.index[0]).total_seconds())
            df_i.insert(0,'rel_time',time_d)       
            st3_list.append(df_i)
        if df_full_cols.loc[df_full_cols['cycle_num']==i]['state'][0] =='STATE4a':
            cycle_index_num=np.linspace(0,num-1,num,dtype=int)
            df_i=df_full_cols.loc[df_full_cols['cycle_num']==i]
            df_i.insert(1,'cycle index',cycle_index_num)
            time_d=[]
            for j in range(0,num):
                time_d.append((df_i.index[j]-df_i.index[0]).total_seconds())
            df_i.insert(0,'rel_time',time_d)          
            st4a_list.append(df_i)
        if df_full_cols.loc[df_full_cols['cycle_num']==i]['state'][0] =='STATE4b':
            cycle_index_num=np.linspace(0,num-1,num,dtype=int)
            df_i=df_full_cols.loc[df_full_cols['cycle_num']==i]
            df_i.insert(1,'cycle index',cycle_index_num)
            time_d=[]
            for i in range(0,num):
                time_d.append((df_i.index[i]-df_i.index[0]).total_seconds())
            df_i.insert(0,'rel_time',time_d)            
            st4b_list.append(df_i)
        if df_full_cols.loc[df_full_cols['cycle_num']==i]['state'][0] =='STATE4c':
            cycle_index_num=np.linspace(0,num-1,num,dtype=int)
            df_i=df_full_cols.loc[df_full_cols['cycle_num']==i]
            df_i.insert(1,'cycle index',cycle_index_num)
            time_d=[]
            for j in range(0,num):
                time_d.append((df_i.index[j]-df_i.index[0]).total_seconds())
            df_i.insert(0,'rel_time',time_d)        
            st4c_list.append(df_i)
     
    min_list=[]
    for i in range(0,len(ave_list)):
        min_list.append(len(ave_list[i]))
        
    min_array=np.asarray(min_list)
    min_length=np.min(min_array[np.nonzero(min_array)])   
    
    cut_ave_list=[]
    for i in range(0,len(ave_list)):
        cut_ave_list.append(ave_list[i][0:min_length])
        



        
    mean_list=[]
    std_list=[]
    for i in range(0,len(ave_list)):
        if len(cut_ave_list[i])!=0:
            mean_list.append(pd.concat(cut_ave_list[i]).groupby('cycle index').mean())
            std_list.append(pd.concat(cut_ave_list[i]).groupby('cycle index').std())
            k=0
            if len(mean_list[-1])!=len(cut_ave_list[i][0]['state'].tolist()):

                while len(mean_list[-1])!=len(cut_ave_list[i][k]['state'].tolist()) and k < len(cut_ave_list[i]):
                    k=k+1

            mean_list[-1]['state']=cut_ave_list[i][k]['state'].tolist()
    #        std_list[-1]['state']=cut_ave_list[i][0]['state'].tolist()
    
    for i in range(0,len(std_list)):
        del mean_list[i]['cycle_num']
        del std_list[i]['cycle_num']
        new_cols=[x+'_ave' for x in mean_list[i].columns[0:-1].tolist()]+[mean_list[i].columns[-1]]
    #    new_cols_std=[x+'_std' for x in mean_list[i].columns[0:-1].tolist()]+[mean_list[i].columns[-1]]
        new_cols_std=[x+'_std' for x in mean_list[i].columns[0:-1].tolist()]
        mean_list[i].columns=new_cols
        std_list[i].columns=new_cols_std
    
    mean_list_state=[]
    for i in range(0,len(mean_list)):
        mean_list_state.append(mean_list[i]['state'][0])
    
    average_state_list=[]
    for i in range(0,len(mean_list)):
        average_state_list.append(pd.concat((mean_list[i],std_list[i]),axis=1))
    
    for i in range(1,len(average_state_list)):
        if average_state_list[i-1]['TI16_ave'][-1:].values[0] == average_state_list[i]['TI16_ave'][0:].values[0]:
            average_state_list[i]=average_state_list[i].drop(0)
            average_state_list[i].reset_index()
            
    print(str(len(average_state_list)))
    
    if len(average_state_list)>=5:
        average_state_list[1]=average_state_list[1][1:3]
        average_state_list[1].reset_index()
        average_state_list[1]['rel_time_ave']=average_state_list[1]['rel_time_ave'].values+average_state_list[0]['rel_time_ave'].values[-1:][0]     
        i=1
        while i <= len(average_state_list)-2:
            average_state_list[i+1]['rel_time_ave']=average_state_list[i+1]['rel_time_ave'].values+average_state_list[i]['rel_time_ave'].values[-1:][0]
            i=i+1
            print(i)
    else:

        average_state_list[1]=average_state_list[1][1:-1]    
        average_state_list[1].reset_index()
        average_state_list[1]['rel_time_ave']=average_state_list[1]['rel_time_ave'].values+average_state_list[0]['rel_time_ave'].values[-1:][0]     
        

    
    full=pd.concat(average_state_list,ignore_index=True)
    
    
#    ST1_ave=full.loc[full['state']=="STATE1"]
#    ST2a_ave=full.loc[full['state']=="STATE2a"]
#    ST2b_ave=full.loc[full['state']=="STATE2b"]
#    ST2c_ave=full.loc[full['state']=="STATE2c"]
#    ST3_ave=full.loc[full['state']=="STATE3"]
#    ST4a_ave=full.loc[full['state']=="STATE4a"]
#    ST4b_ave=full.loc[full['state']=="STATE4b"]
#    ST4c_ave=full.loc[full['state']=="STATE4c"]
    
    return full    
#%%
def create_averaged_plot(update_plot_num,f,full_var_list,full_list,a,df,df_steady,self,canvas,var2,year_var,month_var,day_var,hour_var,min_var,sec_var,end_hour_var,end_min_var,end_sec_var,auto_axis_var,plot_var,
                         steady_year_var,steady_month_var,steady_day_var,steady_hour_var,steady_min_var,steady_sec_var,steady_end_hour_var,steady_end_min_var,steady_end_sec_var,
                          cycle_start_var,cycle_end_var,
                          ST1_ave_var,ST3_ave_var,
                          cycle_time):
    var_states=[]
    for i in range(0,len(full_var_list)):
        var_states.append(full_var_list[i].get())   
        
    plot_vars=[]
    for i in range(0,len(var_states)):
        if var_states[i]==1:
            plot_vars.append(full_list[i])
    
    f.clear()
    a=f.add_subplot(211)
    a.xaxis_date()
    hfmt=dates.DateFormatter('%H:%M:%S')
    a.xaxis.set_major_formatter(hfmt)
    
    add_steady(1,f,df,full_var_list,full_list,a,df_steady,self,canvas,var2,year_var,month_var,day_var,hour_var,min_var,sec_var,end_hour_var,end_min_var,end_sec_var,auto_axis_var,plot_var,
               steady_year_var,steady_month_var,steady_day_var,steady_hour_var,steady_min_var,steady_sec_var,steady_end_hour_var,steady_end_min_var,steady_end_sec_var)
    

    
    start=int(cycle_start_var.get())
    end=int(cycle_end_var.get())
    
    full = average_cycle(start,end,df)
    
    [Q_C1_ave,Q_H1_ave,Q_C2_ave,Q_H2_ave,Q_C1_std,Q_H1_std,Q_C2_std,Q_H2_std,half_cycle_time_ave]=calc_Q(start,end,df)
    

    
    print_ave_value(full,full_var_list,full_list,var2,ST1_ave_var,ST3_ave_var)
    
    
    
    a2=f.add_subplot(212)

    for i in range(0,len(plot_vars)):
        a2.errorbar(full.index,full[plot_vars[i]+'_ave'],yerr=full[plot_vars[i]+'_std'],fmt='-o',capsize=4,markersize=3)
    canvas.show()
    
    ave_for_fit(full,cycle_time,Q_C1_ave,Q_H1_ave,Q_C2_ave,Q_H2_ave,Q_C1_std,Q_H1_std,Q_C2_std,Q_H2_std,half_cycle_time_ave)
#%%
def remove_subplot(update_plot_num,f,full_var_list,full_list,a,df,df_steady,self,canvas,var2,year_var,month_var,day_var,hour_var,min_var,sec_var,end_hour_var,end_min_var,end_sec_var,auto_axis_var,plot_var):
    f.clear()
    a=f.add_subplot(111)
    update_plot(update_plot_num,f,full_var_list,full_list,a,df,df_steady,self,canvas,var2,year_var,month_var,day_var,hour_var,min_var,sec_var,end_hour_var,end_min_var,end_sec_var,auto_axis_var,plot_var)
#%%

def create_subplot(update_plot_num,f,full_var_list,full_list,a,df,df_steady,self,canvas,var2,year_var,month_var,day_var,hour_var,min_var,sec_var,end_hour_var,end_min_var,end_sec_var,auto_axis_var,plot_var):
    f.clear()
    a=f.add_subplot(211)
    a.xaxis_date()
    hfmt=dates.DateFormatter('%H:%M:%S')
    a.xaxis.set_major_formatter(hfmt)
    a2=f.add_subplot(212)
    a2.xaxis_date()
    a2.xaxis.set_major_formatter(hfmt)
    update_plot(update_plot_num,f,full_var_list,full_list,a,df,df_steady,self,canvas,var2,year_var,month_var,day_var,hour_var,min_var,sec_var,end_hour_var,end_min_var,end_sec_var,auto_axis_var,plot_var)

#%%
def BV_range_update(f,BV,BV_start_var,BV_end_var,auto_axis_var,hour_var,min_var,sec_var,end_hour_var,end_min_var,end_sec_var):
    a=f.get_children()[1]
    auto_axis_var_states=[]
    for i in range(0,len(auto_axis_var)):
        auto_axis_var_states.append(auto_axis_var[i].get())
        
    BV_start_index=int(BV_start_var.get())
    BV_end_index=int(BV_end_var.get())
    
    x_start=BV.index[BV_start_index]
    x_end=BV.index[BV_end_index]
    
    if auto_axis_var_states[0]==1:
        a.set_xlim(left=x_start)
        
    hour_var.set(x_start.hour)
    min_var.set(x_start.minute)
    sec_var.set(x_start.second)
    
    if auto_axis_var_states[1]==1:
        a.set_xlim(right=x_end)

    end_hour_var.set(x_end.hour)
    end_min_var.set(x_end.minute)
    end_sec_var.set(x_end.second)
   
#%%
def find_closest_cycle(f,year_var,month_var,day_var,hour_var,min_var,sec_var,end_hour_var,end_min_var,end_sec_var,BV,BV_start_var,BV_end_var):  

    a=f.get_children()[1]
    x_start=matplotlib.dates.num2date(a.get_xlim()[0])

    x_end=matplotlib.dates.num2date(a.get_xlim()[1])

    xx_start=datetime.datetime(x_start.year,x_start.month,x_start.day,x_start.hour,x_start.minute,x_start.second)  
    
    xx_end=datetime.datetime(x_end.year,x_end.month,x_end.day,x_end.hour,x_end.minute,x_end.second)    

                          
    start_cycle_index=np.argmin(np.abs(BV.index.to_pydatetime() -xx_start))        

    end_cycle_index=np.argmin(np.abs(BV.index.to_pydatetime() -xx_end))     
        
    hour_var.set(BV.index[start_cycle_index].hour)
    min_var.set(BV.index[start_cycle_index].minute)
    sec_var.set(BV.index[start_cycle_index].second)
    
    end_hour_var.set(BV.index[end_cycle_index].hour)
    end_min_var.set(BV.index[end_cycle_index].minute)
    end_sec_var.set(BV.index[end_cycle_index].second)
    
    BV_start_var.set(str(start_cycle_index))
    BV_end_var.set(str(end_cycle_index))
#%%                                 #%%
def getxlim(f,year_var,month_var,day_var,hour_var,min_var,sec_var,end_hour_var,end_min_var,end_sec_var):
    a=f.get_children()[1]
    x_start=matplotlib.dates.num2date(a.get_xlim()[0])
    hour_var.set(x_start.hour)
    min_var.set(x_start.minute)
    sec_var.set(x_start.second)
    
    x_end=matplotlib.dates.num2date(a.get_xlim()[1])
    end_hour_var.set(x_end.hour)
    end_min_var.set(x_end.minute)
    end_sec_var.set(x_end.second)
#%%                                  
                                      
def clear_states(var_list):
    for j in range(0,len(var_list)):
        for i in range(0,len(var_list[j])):
            var_list[j][i].set(0)

    
#%%
def update_plot(update_plot_num,f,var,col_list,a,df,df_steady,self,canvas,var2,year_var,month_var,day_var,hour_var,min_var,sec_var,end_hour_var,end_min_var,end_sec_var,auto_axis_var,plot_var):
    a=f.get_children()[update_plot_num]
    a.clear()
    
#    a=f.add_subplot(111)
    
    var_states=[]
    for i in range(0,len(var)):
        var_states.append(var[i].get())             
        
    var2_states=[]
    for i in range(0,len(var2)):
        var2_states.append(var2[i].get())    
        
    plot_vars=[]
    for i in range(0,len(var_states)):
        if var_states[i]==1:
            plot_vars.append(col_list[i])
    
    auto_axis_var_states=[]
    for i in range(0,len(auto_axis_var)):
        auto_axis_var_states.append(auto_axis_var[i].get())
    

    a.xaxis_date()
    hfmt=dates.DateFormatter('%H:%M:%S')
    a.xaxis.set_major_formatter(hfmt)
    leg_loc=2
    if len(var2)==2:
        if var2_states[0]==1 and var2_states[1]==0: 
            for i in range(0,len(plot_vars)):
                if plot_var.get()==0:
                    a.plot(df.index,df[plot_vars[i]],label=plot_vars[i])
                    a.legend(bbox_to_anchor=(1,1), loc=leg_loc,fontsize=10)
                if plot_var.get()==1:
                    a.plot(df.index,df[plot_vars[i]],'o',label=plot_vars[i],markersize=4)
                    a.legend(bbox_to_anchor=(1,1), loc=leg_loc,fontsize=10)
                if plot_var.get()==2:
                    a.plot(df.index,df[plot_vars[i]],'-o',label=plot_vars[i],markersize=4)
                    a.legend(bbox_to_anchor=(1,1), loc=leg_loc,fontsize=10)


#                lna.set_xdata(df.index)
#                lna.set_ydata(df[plot_vars[i]])
    
                
        if var2_states[0]==1 and var2_states[1]==1: 
            for i in range(0,len(plot_vars)):                
                if plot_var.get()==0:
                    a.plot(df.index,df[plot_vars[i]],label=plot_vars[i])
                    a.plot(df_steady.index,df_steady[plot_vars[i]],label=plot_vars[i])
                    
                if plot_var.get()==1:
                    a.plot(df.index,df[plot_vars[i]],'o',label=plot_vars[i],markersize=4)
                    a.plot(df_steady.index,df_steady[plot_vars[i]],label=plot_vars[i])

                if plot_var.get()==2:
                    a.plot(df.index,df[plot_vars[i]],'-o',label=plot_vars[i],markersize=4)
                    a.plot(df_steady.index,df_steady[plot_vars[i]],label=plot_vars[i])
                    
                a.legend(bbox_to_anchor=(1,1), loc=leg_loc,fontsize=10)
        if var2_states[0]==0 and var2_states[1]==1: 
            for i in range(0,len(plot_vars)):
                if plot_var.get()==0:
                    a.plot(df_steady.index,df_steady[plot_vars[i]],label=plot_vars[i])
                if plot_var.get()==1:
                    a.plot(df_steady.index,df_steady[plot_vars[i]],'o',label=plot_vars[i],markersize=4)                    
                if plot_var.get()==2:
                    a.plot(df_steady.index,df_steady[plot_vars[i]],'-o',label=plot_vars[i],markersize=4)
                    
                a.legend(bbox_to_anchor=(1,1), loc=leg_loc,fontsize=10)
    else:
        for i in range(0,len(plot_vars)):
                if plot_var.get()==0:
                    a.plot(df.index,df[plot_vars[i]],label=plot_vars[i])
                    a.legend(bbox_to_anchor=(1,1), loc=leg_loc,fontsize=10)
                if plot_var.get()==1:
                    a.plot(df.index,df[plot_vars[i]],'o',label=plot_vars[i],markersize=4)
                    a.legend(bbox_to_anchor=(1,1), loc=leg_loc,fontsize=10)
                if plot_var.get()==2:
                    a.plot(df.index,df[plot_vars[i]],'-o',label=plot_vars[i],markersize=4)
                    a.legend(bbox_to_anchor=(1,1), loc=leg_loc,fontsize=10)

    

    for i in range(0,len(f.get_children())):
        if str(type(f.get_children()[i]))=="<class 'matplotlib.axes._subplots.AxesSubplot'>":
            sub=f.get_children()[i]
            if auto_axis_var_states[0]==1:
                x_start=datetime.datetime(int(year_var.get()),int(month_var.get()),int(day_var.get()),int(hour_var.get()),int(min_var.get()),int(sec_var.get()))
                sub.set_xlim(left=x_start)
            else:
                x_start=matplotlib.dates.num2date(sub.get_xlim()[0])
                hour_var.set(x_start.hour)
                min_var.set(x_start.minute)
                sec_var.set(x_start.second)
                
            if auto_axis_var_states[1]==1:
                x_end=datetime.datetime(int(year_var.get()),int(month_var.get()),int(day_var.get()),int(end_hour_var.get()),int(end_min_var.get()),int(end_sec_var.get()))
                sub.set_xlim(right=x_end)
            else:
                x_end=matplotlib.dates.num2date(sub.get_xlim()[1])
                end_hour_var.set(x_end.hour)
                end_min_var.set(x_end.minute)
                end_sec_var.set(x_end.second)
    
        
    canvas.show()
#%%
def get_states(var):
    var_states=[]
    for i in range(0,len(var)):
        var_states.append(var[i].get())
        
    return var_states
#%%

def changeExchange(toWhat,pn):
    global exchange
    global DatCounter
    global programName

    exchange = toWhat
    programName=pn
    DatCounter=9000    



def select_file():
    window=tk.Tk()
    window.filename = filedialog.asksaveasfilename()
    save_as_name=window.filename
    window.destroy()
    return save_as_name

def save_averaged_data(df,cycle_start_var,cycle_end_var):  
    sfile=select_file()
    if sfile == '':
        return
    else:
        start=int(cycle_start_var.get())
        end=int(cycle_end_var.get())
        full = average_cycle(start,end,df)
        full.to_csv(sfile)