import glob
import rasterio
import numpy as np
import matplotlib.pyplot as plt

def read_rasterio(filename):
    with rasterio.open(filename) as f:
        data=f.read()
        meta=f.meta
    return data[0], meta


def bit_wise(mask, pos):
    tmp=(mask/(2**pos)).astype('uint8')
    result=tmp-((tmp/2)).astype('uint8')*2
    return result

def mask_invalid(data):
    cloud_pos=1;     shadow_pos=3;    water_pos=5; adj_pos=2;snow_pos=4
    aerosol_bit_1=6;aerosol_bit_2=7

    cloud= bit_wise(data,cloud_pos)
    shadow=bit_wise(data,shadow_pos)
    water= bit_wise(data,water_pos)
    adj=bit_wise(data,adj_pos)

    snow=bit_wise(data,snow_pos)

    aerosol_1=bit_wise(data,aerosol_bit_1)
    aerosol_2=bit_wise(data,aerosol_bit_2)

    shapes=data.shape

    mask=np.zeros([shapes[0], shapes[1]], dtype=np.uint8)+1
    mask[cloud==1]=2
    mask[shadow==1]=3
    mask[water==1]=5
    mask[adj==1]=2
    mask[snow==1]=2

    return mask


def read_hls(hls_dir, aimed_bands=None):

    if aimed_bands is None:
        files=glob.glob(hls_dir+'*.tif')

        aimed_bands=\
                sorted([x.split('/')[-1].split('.tif')[0].split('.')[-1] \
                for x in files])

    record=[]
    for aimed_band in aimed_bands:
        filename=glob.glob(hls_dir+'*'+aimed_band+'*tif')
        if len(filename)!=1:
            print('no geotif file was found for '+aimed_band)
            return 

        with rasterio.open(filename[0]) as f:
            data=f.read(1)

        if aimed_band=='Fmask':
            data=mask_invalid(data)

        record.append(data)

    record=np.stack(record)
    return record,aimed_bands



if __name__=="__main__":

    hls_dir='/mnt/scratch/huangh33/hls_data_2.0/DRC/T34LFQ/HLS.S30.T34LFQ.2024143T082559.v2.0/'
    aimed_bands=['B8A','B11','B12', 'Fmask']

    hlsdata=read_hls(hls_dir)

    if not hlsdata is None:
        record, bandnames=hlsdata[0], hlsdata[1]





            
    
        








