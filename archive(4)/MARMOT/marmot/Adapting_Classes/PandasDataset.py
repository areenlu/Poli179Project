#!/usr/bin/env python
# coding: utf-8

# In[1]:


from torch.utils.data import Dataset

class PandasDataset(Dataset):
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def __len__(self):
        return len(self.dataframe)

    def __getitem__(self, index):
        print('list')
        print((self.dataframe.iloc[index].tolist()))
        print('item')
        print((self.dataframe.iloc[index]))
        return self.dataframe.iloc[index].tolist()

