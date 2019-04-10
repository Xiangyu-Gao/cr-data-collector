import os
import datetime

def Packet_reorder_zerofill(file_dir, file_out_name):
    log_dir = 'D:\\tmp\\radar_pp\\log.txt'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    #print(file_dir)
    #print(file_out_name)
    command = 'C:\\ti\\mmwave_studio_01_00_00_00\\mmWaveStudio\\PostProc\\Packet_Reorder_Zerofill.exe ' \
                + file_dir + ' ' + file_out_name + ' ' + log_dir
    os.system(command)
    
def reorder_zerofill_for_seq(folder_dir):
    file_names = sorted(os.listdir(folder_dir))
    folder_out_dir = folder_dir.replace('radar', 'rad_reo_zerf')

    if not os.path.exists(folder_out_dir):
        os.makedirs(folder_out_dir)
    
    for file_name in file_names:
        index = file_name[-5];
        file_dir = os.path.join(folder_dir, file_name)

        file_out_name = os.path.join(folder_out_dir, 'adc_data_' + index + '.bin')

        file_reo_zef = Packet_reorder_zerofill(file_dir, file_out_name)

def reorder_zerofill_for_date(date, data_dir='D:\\RawData'):
    base_dir = os.path.join(data_dir, date)

    if not os.path.exists(base_dir):
        raise ValueError("Data not found!")

    seqs = sorted(os.listdir(base_dir))
    for seq in seqs:
        folder_dir = os.path.join(base_dir, seq, 'radar')
        print("Packet reorder and zerofill %s ..." % folder_dir)
        reorder_zerofill_for_seq(folder_dir)

    print("\nPacket reorder and zerofill finished for date %s." % date)

if __name__ == '__main__':

    # main("D:/RawData/0000/images", 'ost.yaml')
    # load_calib('ost.yaml')

    date = input("Enter date (default=today): ")
    if date == '':
        now = datetime.datetime.now()
        date = "%s_%02d_%02d" % (now.year, now.month, now.day)

    reorder_zerofill_for_date(date)
