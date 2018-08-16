这是17年参加全国智慧城市大赛的一个赛题，车辆精确识别，整理了一些相关文档放在其中。我们在VGG模型的基础上对损失函数做了改进。 我们用的是“Deep Relative Distance Learning: Tell the Difference Between Similar Vehicles”中提出的“Coupled Clusters Loss”。
![Image text](https://github.com/lli27/Accurate-identification-for-vehicles/blob/master/车辆精确识别/loss.png)

它度量的是簇中正样本的中心点与距簇最近的负样本之间的距离。
