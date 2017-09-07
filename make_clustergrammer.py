'''
Python 2.7
The clustergrammer python module can be installed using pip:
pip install clustergrammer

or by getting the code from the repo:
https://github.com/MaayanLab/clustergrammer-py
'''

from clustergrammer import Network
import pandas as pd
import numpy as np
net = Network()

# load matrix tsv file
net.load_file('txt/rc_two_cats.txt')
# net.load_file('txt/ccle_example.txt')
# net.load_file('txt/rc_val_cats.txt')
# net.load_file('txt/number_labels.txt')
# net.load_file('txt/mnist.txt')
# net.load_file('txt/tuple_cats.txt')
# net.load_file('txt/example_tsv.txt')

net.swap_nan_for_zero()
df = net.export_df()
print(df.shape)

# scale dna right to left
###################
cols = df.columns.tolist()
num_cols = len(cols)
for inst_col in cols:
    inst_val = float(inst_col[1])
    df[inst_col] = df[inst_col] * inst_val/float(num_cols)*4.2

# net.enrichrgram('KEA_2015')

noise = pd.DataFrame(np.random.randint(0, 50,size=( 103, 72)))

# scale down and center mat
noise = noise/20
noise = noise - noise.mean()


# scale noise from left to right
###################
cols = noise.columns.tolist()
num_cols = len(cols)
for inst_col in cols:
    index = num_cols - inst_col - 10
    if index < 0:
      index = 0
    noise[inst_col] = noise[inst_col] * ((index)/float(num_cols) + 0.05 )

noise_mat = noise.as_matrix()

dna_mat = df.as_matrix()
dna_mat = dna_mat * 0.8

new_mat = dna_mat + noise_mat

df.data = new_mat

cols = df.columns.tolist()
rows = df.index.tolist()

new_df = pd.DataFrame(data=new_mat)
new_df.columns = cols
new_df.index = rows
print(new_mat.shape)
print(df.shape)

net.load_df(new_df)

# optional filtering and normalization
##########################################
# net.filter_sum('row', threshold=20)
# net.normalize(axis='col', norm_type='zscore', keep_orig=True)
# net.filter_N_top('row', 250, rank_type='sum')
# net.filter_threshold('row', threshold=0.01, num_occur=4)
net.swap_nan_for_zero()
# net.set_cat_color('col', 1, 'Category: one', 'blue')

  # net.make_clust()
  # net.dendro_cats('row', 5)

net.cluster(dist_type='cos',views=['N_row_sum', 'N_row_var'] , dendro=True,
               sim_mat=True, filter_sim=0.1, calc_cat_pval=False, enrichrgram=True, run_clustering=True)

# write jsons for front-end visualizations
net.write_json_to_file('viz', 'json/mult_view.json', 'indent')
# net.write_json_to_file('sim_row', 'json/mult_view_sim_row.json', 'no-indent')
# net.write_json_to_file('sim_col', 'json/mult_view_sim_col.json', 'no-indent')
