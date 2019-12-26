#### GTree Linux Version QA
1. I dont want to compile GTree and just want to run GTree.

    A: Just download GTree_Linux zip file,decompress, open terminal in GTree_Linux directory, input 'sh ./run_local.sh' and run GTree.

2. I cannot run GTree in Linux.
   
   A: We test GTree in Ubuntu 16.04 and 18.04 with NVidia GPU. The compiler GCC version is 5.4. Please check you have installed GPU driver. 
   If you still have problem, please submit Issue on Github.

3. What's the difference between the binary threshold value of NeuroGPS and Axon?
   
   A: The binary threshold value of NeuroGPS is used for soma localization (NeuroGPS method) and local neuron population tracing (NeuroGPS-Tree method). The binary threshold value of Axon is used for GTree brain-wide neuron tracing. 

4. How to decide the binary threshold value of NeuroGPS and Axon?
   
   A: Please click the corresponding button 'preview' to see the binary image result. That will help for tuning binary parameters.

5. GTree donot find neurite branches.

    A: It is caused by signal detection failure.You can test the following operation:
       (1) Please fine-tune your binary threshold first. 
       (2) Cancel 'Strong noise' in Axon table.
       (3) Turn down Axon bifur value.
       (4) Turn up max bound num.
       (5) Tick 'Enable SVM' in Axon table.

6. Where is difference localization module?
   
   A: Please input 2 or more trees. Go to Editor table in 'BinarySettingDockWidget' and right click the tree which the active status is disable (d). Click 'compare_tree'. The active Tree and  clicked Tree will be used for difference localization. Right click the 'checked' table below and tick 'show arrow'.

7. How can I use deep learning?

    A: Sorry, deep learning part have not been completed.

8. What are 'Debug','NewFuncTest' and 'Tool' menu used for?

    A: GTree is still in developing. They are debugging unit. Please donot use them.

9. How large the tiff file can I input to GTree?

    A: We suggest using tiff file under 2 GB. If you want to use tracing module, that depends on neurite density and we cannot give a precise result. Now we are working on resolving the structure of images which include densely distributed neurites.

10. It is difficult to read the code.

    A: That's a story. 