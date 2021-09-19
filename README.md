

The code is as follows:

1) AIA: Attribute inference attacks. The embeddings are already generated using code form their original repos.

2) MIA: Membership Inference attacks. The code is divided into blackbox (includes confidence score attacks and shadow model attack) and whitebox. MIA in blackbox setting is performed on inductive training of GraphSage model. 

3) Reconstruction: Graph Reconstruction using graph encoder decoder.

Data: The facebook and LastFM dataset for attribute inference attacks is available from Stanford Large Network Datasete Collection. The data for graph reconstruction requires to load the train and test graphs seperately unlike what most libraries provider. The data can be obtained from https://github.com/DaehanKim/vgae_pytorch.


