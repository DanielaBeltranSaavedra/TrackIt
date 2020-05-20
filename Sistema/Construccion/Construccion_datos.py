
# Definition of class for data interaction
class Historical:
    def __init__(self,loan_sequence_number):
        self.loan_sequence_number=loan_sequence_number
        
# Definition of class for data interaction
class Output:
    def __init__(self,loan_sequence_number,repurchase_flag,current_loan_delinquency_status_repurchase_flag,
    later_payment_flag,current_loan_delinquency_status_later_payment,later_payment_flag_percentage,times_repurchase_flag,times_later_payment):
      self.loan_sequence_number=loan_sequence_number
      self.repurchase_flag=repurchase_flag
      self.current_loan_delinquency_status_repurchase_flag=current_loan_delinquency_status_repurchase_flag
      self.later_payment_flag=later_payment_flag
      self.current_loan_delinquency_status_later_payment=current_loan_delinquency_status_later_payment
      self.times_repurchase_flag=times_repurchase_flag
      self.times_later_payment=times_later_payment
      self.later_payment_flag_percentage=later_payment_flag_percentage

      
list =[]


with open("harp_historical_data1_time.txt", "r") as filestream: #Reading the file
     a=[]
     #for line in filestream: #To read the whole file
     for i in range(50): #Determine the number of lines for testing
            line= filestream.readline() #Determine the number of lines for testing
            # Creating and separating data
            currentline = line.split("|")
            loan_sequence_number=currentline[0]
            monthly_reporting_period=currentline[1]
            current_actual_upb=currentline[2]
            current_loan_delinquency_status=currentline[3]
            loan_age =currentline[4]
            remaining_months_to_legal_maturity=currentline[5]
            repurchase_flag=currentline[6]
            modification_flag=currentline[7]
            zero_balance_code=currentline[8]
            zero_balance_effective_date=currentline[9]
            current_interest_rate=currentline[10]
            current_deferred_upb=currentline[11]
            due_date_of_last_paid_istallment=currentline[12]
            mi_recoveries=currentline[13]
            net_sales_proceeds=currentline[14]
            non_mi_recoveries=currentline[15]
            expenses=currentline[16]
            legal_cost=currentline[17]
            maintenance_and_perservation_costs=currentline[18]
            taxes_and_insurance=currentline[19]
            miscellaneous_expenses=currentline[20]
            actual_loss_calculation=currentline[21]
            modification_cost=currentline[22]
            step_modification_flag=currentline[23]
            deferred_payment_modification=currentline[24]
            
            #Creation of rules to create new data based on time performance
            if loan_sequence_number not in a:
              
              a.append(loan_sequence_number)
              loan_sequence_number=loan_sequence_number
              
              repurchase_flag='Y'
              current_loan_delinquency_status_repurchase_flag=current_loan_delinquency_status
              times_repurchase_flag=0

              later_payment_flag='N'
              current_loan_delinquency_status_later_payment='N'
              times_later_payment=0
              later_payment_flag_percentage=' '
              outputPerson=Output (loan_sequence_number,repurchase_flag,current_loan_delinquency_status_repurchase_flag,
              later_payment_flag,current_loan_delinquency_status_later_payment,later_payment_flag_percentage,times_repurchase_flag,times_later_payment)
              list.append(outputPerson)
            else :
                  #Generation of new data in to write in the file
                  for obj in list:
                    if obj.loan_sequence_number == loan_sequence_number:
                      if repurchase_flag == 'N':
                          if obj.repurchase_flag != 'N':
                              obj.repurchase_flag='N'
                              obj.current_loan_delinquency_status_repurchase_flag=current_loan_delinquency_status
                              obj.times_repurchase_flag+=1
                          else:
                               obj.times_repurchase_flag+=1
                      else:
                          if obj.repurchase_flag == 'N':
                              obj. repurchase_flag='N'
                              obj.current_loan_delinquency_status_repurchase_flag=current_loan_delinquency_status
                              obj.times_repurchase_flag+=1
                              obj.later_payment_flag_percentage=current_actual_upb
                              
#Creating and writing the output file with new data
outputFile=open("outputFile.txt","w+")
for obj in list:
   outputFile.write(obj.loan_sequence_number + '|' + obj.repurchase_flag + '|' + obj.current_loan_delinquency_status_repurchase_flag + '|' 
   + obj.later_payment_flag + '|' + obj.current_loan_delinquency_status_later_payment + '|' + obj.later_payment_flag_percentage + '|' + str(obj.times_repurchase_flag) + '|' + str(obj.times_later_payment )+'\n')         

outputFile.close()
