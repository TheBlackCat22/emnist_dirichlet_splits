## Instructions

1. Activate your virtual python environment (conda or venv)
2. Run the get_data.sh shell script by:  
`bash get_data.sh`  
This will download the raw Emnist data and process the byclass split of the dataset into .png files.
3. Run the code/make_dirichlet_splits.py script with the arguments alpha, num_clients. eg:  
`python code/make_dirichlet_splits.py --alpha 0.3 --num_clients 10`  
4. In the splits directory, you will find all required splits in image_list.txt files.