import numpy as np
from subprocess import Popen
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--alpha", type=float, default=None)
parser.add_argument("--num_clients", type=int, default=None)
parser.add_argument("--num_classes", type=int, default=62)
args = parser.parse_args()


def dirichlet_split(labels, path, args):
    
    alpha = args.alpha
    num_clients = args.num_clients
    Popen(f'bash splits/make_folders.sh {str(alpha)} {str(num_clients)} {str(args.num_classes)}', shell=True)

    NUM_CLASS = len(np.unique(labels))
    MIN_SIZE = 0
    idx = [np.where(labels==i)[0] for i in range(NUM_CLASS)]
    path = path + f"/alpha_{str(alpha)}"
    
    while MIN_SIZE < 10:
        idx_batch = [[] for _ in range(num_clients)]
        for k in range(NUM_CLASS):
            print(f"-Class {k}")
            class_path = path + f"/class_{str(k)}"
            np.random.shuffle(idx[k])
            distributions = np.random.dirichlet(np.repeat(alpha, num_clients))
            distributions = np.array(
                [
                    p * (len(idx_j) < len(labels) / num_clients)
                    for p, idx_j in zip(distributions, idx_batch)
                ]
            )
            distributions = distributions / distributions.sum()
            distributions = (np.cumsum(distributions) * len(idx[k])).astype(int)[:-1]
            idx_batch = [
                np.concatenate((idx_j, idx.tolist())).astype(np.int64)
                for idx_j, idx in zip(idx_batch, np.split(idx[k], distributions))
            ]
            MIN_SIZE = min([len(idx_j) for idx_j in idx_batch])
            
            for i in range(num_clients):
                client_path = class_path + f"/client_{str(i)}"
                with open(client_path + "/image_list.txt", 'w') as f:
                    for item in idx_batch[i]:
                        f.write(f"{item}.png\n")
                # np.savetxt(client_path + "/image_list.txt", idx_batch[i], fmt='%s')


train_labels = np.loadtxt("emnist_byclass/Processed/train_labels", np.int64)

if (args.alpha is not None) and (args.num_clients is not None):
    dirichlet_split(train_labels, "splits", args)
else:
    print("Please give arguments properly")
