# -*- coding: utf-8 -*-
"""------------------------------------------------- File Name：  DouglasPeuker Description : 道格拉斯-普克抽稀算法 Author :    J_hao date：     2017/8/16------------------------------------------------- Change Activity:         2017/8/16: 道格拉斯-普克抽稀算法-------------------------------------------------"""
from __future__ import division

from math import sqrt, pow

THRESHOLD = 0.0001 # 阈值


def point2LineDistance(point_a, point_b, point_c):
  """  计算点a到点b c所在直线的距离  :param point_a:  :param point_b:  :param point_c:  :return:  """
  # 首先计算b c 所在直线的斜率和截距
  if point_b[0] == point_c[0]:
    return 9999999
  slope = (point_b[1] - point_c[1]) / (point_b[0] - point_c[0])
  intercept = point_b[1] - slope * point_b[0]

  # 计算点a到b c所在直线的距离
  distance = abs(slope * point_a[0] - point_a[1] + intercept) / sqrt(1 + pow(slope, 2))
  return distance


class DouglasPeuker(object):
  def __init__(self):
    self.threshold = THRESHOLD
    self.qualify_list = list()
    self.disqualify_list = list()

  def diluting(self, point_list):
    """    抽稀    :param point_list:二维点列表    :return:    """
    if len(point_list) < 3:
      self.qualify_list.extend(point_list[::-1])
    else:
      # 找到与收尾两点连线距离最大的点
      max_distance_index, max_distance = 0, 0
      for index, point in enumerate(point_list):
        if index in [0, len(point_list) - 1]:
          continue
        distance = point2LineDistance(point, point_list[0], point_list[-1])
        if distance > max_distance:
          max_distance_index = index
          max_distance = distance

      # 若最大距离小于阈值，则去掉所有中间点。 反之，则将曲线按最大距离点分割
      if max_distance < self.threshold:
        self.qualify_list.append(point_list[-1])
        self.qualify_list.append(point_list[0])
      else:
        # 将曲线按最大距离的点分割成两段
        sequence_a = point_list[:max_distance_index]
        sequence_b = point_list[max_distance_index:]

        for sequence in [sequence_a, sequence_b]:
          if len(sequence) < 3 and sequence == sequence_b:
            self.qualify_list.extend(sequence[::-1])
          else:
            self.disqualify_list.append(sequence)

  def main(self, point_list):
    self.diluting(point_list)
    while len(self.disqualify_list) > 0:
      self.diluting(self.disqualify_list.pop())
    print(self.qualify_list)
    print(len(self.qualify_list))
    print(len(point_list))


if __name__ == '__main__':
  d = DouglasPeuker()
  d.main([[117.212396,39.770742],[117.204106,39.765542],[117.193148,39.761971],[117.185776,39.758029],[117.180766,39.758373],[117.175529,39.755896],[117.173631,39.755647],[117.171157,39.756462],[117.168406,39.753669],[117.169353,39.750307],[117.171932,39.745312],[117.172488,39.744098],[117.171582,39.743193],[117.166921,39.7448],[117.166006,39.742617],[117.161122,39.739325],[117.160713,39.7337],[117.163559,39.729382],[117.167374,39.728287],[117.171905,39.723933],[117.175018,39.727134],[117.172606,39.723397],[117.171374,39.717635],[117.177132,39.714686],[117.176841,39.711128],[117.176004,39.708906],[117.177353,39.705539],[117.1765,39.697525],[117.175082,39.689922],[117.177169,39.679764],[117.171662,39.675627],[117.166233,39.670667],[117.166345,39.666774],[117.169313,39.666128],[117.169617,39.660203],[117.175589,39.658206],[117.175361,39.653251],[117.179749,39.65233],[117.184582,39.649189],[117.179476,39.643281],[117.173759,39.642287],[117.161632,39.638033],[117.158378,39.634505],[117.160652,39.632075],[117.158873,39.631471],[117.155513,39.629259],[117.15273,39.627537],[117.146475,39.626655],[117.147828,39.625061],[117.149599,39.62351],[117.14741,39.6234],[117.138909,39.625376],[117.13338,39.627556],[117.131976,39.62773],[117.131206,39.627794],[117.132905,39.62432],[117.134377,39.623371],[117.127778,39.627903],[117.127723,39.625771],[117.123441,39.627069],[117.119275,39.630922],[117.115579,39.629861],[117.115043,39.629069],[117.10972,39.634041],[117.089654,39.641879],[117.078999,39.646902],[117.073249,39.647437],[117.067839,39.650463],[117.063331,39.651627],[117.048691,39.65359],[117.04208,39.655204],[117.03224,39.658587],[117.027013,39.658808],[117.017936,39.658003],[117.016073,39.655567],[117.014201,39.654755],[117.011317,39.652501],[117.011092,39.651336],[117.00046,39.649044],[116.997826,39.646358],[116.995799,39.646971],[116.993438,39.646471],[116.987386,39.644622],[116.981905,39.643226],[116.981645,39.644477],[116.982046,39.650944],[116.981313,39.652966],[116.980256,39.653566],[116.978189,39.655123],[116.977381,39.655188],[116.976501,39.654366],[116.972928,39.651386],[116.971032,39.649682],[116.969902,39.649792],[116.968284,39.650898],[116.965316,39.655031],[116.963497,39.659628],[116.962126,39.664979],[116.963519,39.670144],[116.959203,39.674739],[116.95305,39.677486],[116.952568,39.680181],[116.952828,39.681974],[116.952639,39.682746],[116.95718,39.683478],[116.953933,39.68742],[116.951426,39.690875],[116.950579,39.693072],[116.951311,39.693843],[116.95221,39.694555],[116.951883,39.697873],[116.95096,39.701456],[116.952749,39.702692],[116.955031,39.707322],[116.957147,39.709247],[116.95223,39.712986],[116.945127,39.71251],[116.942048,39.711516],[116.939954,39.712512],[116.935094,39.712842],[116.924353,39.711502],[116.926682,39.704879],[116.922756,39.70474],[116.920495,39.701997],[116.918686,39.700094],[116.919641,39.698877],[116.919491,39.697541],[116.906332,39.694297],[116.895711,39.694026],[116.89874,39.697372],[116.899739,39.703442],[116.895034,39.706195],[116.8937,39.725504],[116.897735,39.729785],[116.914271,39.734704],[116.924017,39.735949],[116.923405,39.741892],[116.919209,39.744672],[116.91982,39.747408],[116.920177,39.752185],[116.915312,39.761601],[116.909541,39.761258],[116.909837,39.765005],[116.911342,39.770209],[116.915869,39.771779],[116.920127,39.767759],[116.92322,39.769428],[116.924085,39.772377],[116.927794,39.775504],[116.924156,39.780343],[116.923196,39.781197],[116.928021,39.786096],[116.941793,39.787682],[116.94855,39.7864],[116.951711,39.784883],[116.953203,39.783505],[116.956946,39.784471],[116.95517,39.791277],[116.959258,39.792376],[116.96058,39.792475],[116.958454,39.796624],[116.955664,39.797443],[116.947546,39.79918],[116.945173,39.798994],[116.944113,39.801022],[116.943553,39.801406],[116.943812,39.801794],[116.942113,39.805269],[116.942414,39.806851],[116.944919,39.807332],[116.947107,39.807239],[116.950123,39.807547],[116.944337,39.811369],[116.937076,39.817797],[116.935983,39.824015],[116.934394,39.838429],[116.929863,39.847209],[116.920648,39.855658],[116.918513,39.856772],[116.915904,39.856206],[116.915484,39.854887],[116.908659,39.854359],[116.908752,39.848591],[116.913974,39.841177],[116.914351,39.838624],[116.91243,39.836889],[116.905577,39.838422],[116.902057,39.840259],[116.893177,39.850947],[116.891239,39.851796],[116.885266,39.849044],[116.880325,39.850238],[116.879838,39.848844],[116.876508,39.849155],[116.872153,39.853073],[116.864004,39.855292],[116.862529,39.858559],[116.860645,39.861285],[116.860299,39.862412],[116.859452,39.864761],[116.855149,39.864858],[116.850742,39.866544],[116.846176,39.871194],[116.843963,39.87047],[116.831594,39.883834],[116.826519,39.884703],[116.823082,39.885301],[116.820835,39.886873],[116.819659,39.887243],[116.818949,39.894932],[116.814875,39.894839],[116.814419,39.890438],[116.810601,39.884271],[116.80646,39.885298],[116.80445,39.886565],[116.802122,39.887189],[116.797157,39.890132],[116.794646,39.892591],[116.791808,39.896272],[116.791357,39.89775],[116.79051,39.898778],[116.79035,39.902607],[116.790464,39.903892],[116.791369,39.906015],[116.791113,39.90711],[116.791037,39.908289],[116.790538,39.91134],[116.787778,39.914871],[116.787393,39.917225],[116.789469,39.918995],[116.789471,39.926029],[116.788804,39.928581],[116.788339,39.930203],[116.787221,39.934064],[116.787326,39.938473],[116.789078,39.941099],[116.790037,39.942387],[116.79408,39.943012],[116.792847,39.944387],[116.791523,39.944382],[116.792337,39.944953],[116.791791,39.946717],[116.791018,39.946015],[116.791567,39.94769],[116.791831,39.949111],[116.789554,39.949343],[116.787,39.956534],[116.785082,39.959705],[116.784509,39.961784],[116.782589,39.961915],[116.781436,39.964264],[116.780428,39.964519],[116.779262,39.966953],[116.779218,39.963971],[116.779113,39.960824],[116.776019,39.960864],[116.773441,39.961331],[116.768688,39.96384],[116.767817,39.964514],[116.764862,39.965099],[116.763225,39.971154],[116.763827,39.972651],[116.765607,39.973844],[116.768769,39.976747],[116.770319,39.979604],[116.772099,39.981432],[116.772033,39.984117],[116.77179,39.98554],[116.773036,39.98701],[116.774031,39.988434],[116.775932,39.992325],[116.777276,39.994536],[116.780516,39.996623],[116.783102,39.999662],[116.780813,40.003029],[116.781538,40.006783],[116.779271,40.012475],[116.776807,40.015037],[116.776679,40.018625],[116.779821,40.021557],[116.780736,40.02363],[116.782227,40.025597],[116.781138,40.027526],[116.78109,40.029834],[116.780484,40.031669],[116.779718,40.033771],[116.780702,40.035873],[116.784137,40.035807],[116.784399,40.037958],[116.785943,40.038647],[116.787344,40.040461],[116.793975,40.040702],[116.796662,40.039737],[116.80362,40.035984],[116.807121,40.035327],[116.808572,40.035567],[116.81014,40.037712],[116.816908,40.036979],[116.818453,40.038123],[116.818851,40.037069],[116.82203,40.035871],[116.826349,40.03426],[116.827077,40.035969],[116.828447,40.036386],[116.827129,40.039922],[116.827097,40.045409],[116.829965,40.045895],[116.829607,40.051896],[116.835102,40.053446],[116.838166,40.054486],[116.842567,40.056948],[116.855192,40.057703],[116.857221,40.060744],[116.86366,40.058559],[116.862699,40.056442],[116.866194,40.055595],[116.872223,40.050479],[116.876128,40.048225],[116.879313,40.047659],[116.884117,40.049651],[116.887042,40.051136],[116.892312,40.051916],[116.896187,40.052184],[116.898818,40.05231],[116.907627,40.053514],[116.912291,40.056758],[116.914481,40.058286],[116.914998,40.058414],[116.9197,40.05871],[116.922127,40.054327],[116.92349,40.054087],[116.925577,40.050858],[116.929882,40.052872],[116.931704,40.055361],[116.932361,40.05711],[116.93324,40.058438],[116.934633,40.0572],[116.93535,40.057226],[116.936266,40.060915],[116.938155,40.058333],[116.940419,40.057883],[116.942651,40.05644],[116.945548,40.056137],[116.943849,40.054965],[116.94277,40.053862],[116.944779,40.052971],[116.945984,40.051886],[116.949156,40.054283],[116.950159,40.050666],[116.951184,40.051097],[116.951924,40.054196],[116.95252,40.046703],[116.968775,40.056948],[116.971361,40.054611],[116.97468,40.054409],[116.976906,40.051849],[116.978761,40.050471],[116.977461,40.049405],[116.976858,40.046522],[116.974936,40.04377],[116.976612,40.040533],[116.981706,40.043888],[116.994212,40.044462],[117.00297,40.040217],[117.006677,40.036487],[117.011161,40.036715],[117.017578,40.037749],[117.019605,40.039122],[117.021203,40.037018],[117.026144,40.038321],[117.028212,40.035813],[117.030146,40.039167],[117.03421,40.040005],[117.033794,40.044603],[117.041869,40.050303],[117.047449,40.054783],[117.049574,40.056815],[117.055697,40.056513],[117.057646,40.057828],[117.059528,40.058607],[117.059648,40.060544],[117.058598,40.065027],[117.061717,40.064741],[117.063233,40.06625],[117.067954,40.066308],[117.070359,40.067231],[117.07278,40.068842],[117.075872,40.073054],[117.082513,40.073984],[117.087517,40.074417],[117.088827,40.070939],[117.089446,40.073834],[117.091338,40.07475],[117.091837,40.08061],[117.102846,40.080973],[117.104399,40.082161],[117.108267,40.082255],[117.108367,40.0797],[117.109018,40.079695],[117.111525,40.080821],[117.110413,40.07943],[117.113428,40.078126],[117.121507,40.078526],[117.123645,40.077565],[117.125462,40.078744],[117.131923,40.075319],[117.139206,40.070671],[117.143427,40.07053],[117.148433,40.071947],[117.152349,40.072139],[117.157714,40.074162],[117.162542,40.075366],[117.166158,40.081921],[117.162436,40.084156],[117.16494,40.083839],[117.169981,40.081887],[117.171571,40.082377],[117.177374,40.079786],[117.179119,40.078966],[117.180971,40.078895],[117.181674,40.07761],[117.182998,40.077409],[117.18469,40.076756],[117.186465,40.075638],[117.189315,40.077401],[117.191158,40.080575],[117.192388,40.082214],[117.187689,40.085697],[117.189349,40.086976],[117.191653,40.089664],[117.19185,40.090618],[117.194461,40.089927],[117.196393,40.088088],[117.195098,40.085844],[117.197521,40.079582],[117.199729,40.077464],[117.202472,40.076664],[117.204615,40.075607],[117.204289,40.073275],[117.20608,40.074439],[117.210416,40.075704],[117.211805,40.078469],[117.214047,40.082538],[117.209813,40.082597],[117.210379,40.0859],[117.215041,40.088459],[117.217501,40.087245],[117.219197,40.084728],[117.220411,40.081233],[117.221843,40.079178],[117.225609,40.07739],[117.227804,40.074051],[117.228506,40.071548],[117.225276,40.070751],[117.220866,40.071299],[117.217867,40.070314],[117.214537,40.071324],[117.211276,40.06984],[117.208734,40.07048],[117.204358,40.071764],[117.198684,40.071795],[117.198178,40.068464],[117.195666,40.067822],[117.192502,40.067152],[117.189443,40.067325],[117.188084,40.064279],[117.190285,40.060112],[117.191172,40.057697],[117.194957,40.05277],[117.19398,40.051589],[117.193348,40.047754],[117.19341,40.044952],[117.193599,40.040957],[117.194614,40.038221],[117.194434,40.0328],[117.19536,40.030004],[117.198533,40.029053],[117.199779,40.023384],[117.200936,40.020246],[117.202049,40.017811],[117.202468,40.016298],[117.203861,40.015925],[117.20323,40.012261],[117.202132,40.009453],[117.203701,40.005858],[117.204324,40.002064],[117.203415,39.99858],[117.20137,39.99638],[117.199885,39.994947],[117.198143,39.992432],[117.197525,39.987725],[117.196276,39.986525],[117.194709,39.985332],[117.191827,39.983929],[117.186611,39.983513],[117.186048,39.977887],[117.185186,39.975905],[117.186825,39.974811],[117.185602,39.970501],[117.18273,39.965089],[117.180139,39.965843],[117.177178,39.969772],[117.173082,39.969096],[117.168505,39.97187],[117.167295,39.971323],[117.171289,39.969085],[117.171381,39.96797],[117.171892,39.963546],[117.170067,39.957635],[117.159251,39.952659],[117.155133,39.952706],[117.152166,39.952358],[117.155698,39.949817],[117.158723,39.947042],[117.161515,39.943085],[117.160616,39.940696],[117.158398,39.94024],[117.154859,39.942243],[117.150787,39.939473],[117.150875,39.936037],[117.152653,39.931816],[117.154057,39.93087],[117.15123,39.929384],[117.145157,39.927928],[117.140491,39.92775],[117.14068,39.926105],[117.143437,39.925657],[117.147011,39.92469],[117.148482,39.919822],[117.149725,39.916809],[117.154324,39.916157],[117.160944,39.916448],[117.163224,39.914968],[117.162826,39.911722],[117.157339,39.909075],[117.152843,39.904653],[117.152944,39.902874],[117.158177,39.89878],[117.162602,39.894985],[117.1594,39.888993],[117.158429,39.886432],[117.162496,39.884483],[117.166846,39.882849],[117.167981,39.881239],[117.168558,39.879377],[117.170167,39.878255],[117.172464,39.878535],[117.174397,39.881812],[117.174523,39.883568],[117.175978,39.882901],[117.179281,39.880264],[117.177509,39.878241],[117.17101,39.874508],[117.17206,39.87308],[117.177299,39.872095],[117.180204,39.872803],[117.181186,39.875788],[117.182783,39.876406],[117.185832,39.87401],[117.184779,39.871469],[117.185051,39.870138],[117.187367,39.869822],[117.189805,39.871419],[117.191362,39.872454],[117.194766,39.870055],[117.199114,39.867371],[117.202014,39.86769],[117.20614,39.868106],[117.214798,39.866104],[117.216213,39.863851],[117.217607,39.862389],[117.22136,39.863346],[117.229638,39.860599],[117.232422,39.859266],[117.234129,39.85981],[117.235028,39.863127],[117.236183,39.863648],[117.239555,39.862391],[117.242028,39.862566],[117.24324,39.865407],[117.245444,39.866976],[117.249932,39.867734],[117.252098,39.867357],[117.255974,39.86381],[117.255862,39.862281],[117.259342,39.857487],[117.261593,39.85501],[117.263559,39.851685],[117.264492,39.850098],[117.262906,39.849128],[117.260652,39.849338],[117.259465,39.847296],[117.257822,39.84514],[117.259325,39.843575],[117.258835,39.841769],[117.256664,39.840339],[117.257886,39.839169],[117.259974,39.839646],[117.261477,39.836856],[117.245579,39.840195],[117.238852,39.839879],[117.232867,39.837602],[117.22992,39.834637],[117.228182,39.83438],[117.221399,39.838731],[117.21427,39.841241],[117.207204,39.840833],[117.201977,39.839598],[117.203567,39.832134],[117.201546,39.831147],[117.19824,39.832512],[117.177849,39.830346],[117.170871,39.82468],[117.166275,39.825599],[117.167601,39.813477],[117.163065,39.808742],[117.169387,39.804823],[117.179015,39.803703],[117.185404,39.801384],[117.187483,39.788835],[117.193436,39.784948],[117.204223,39.778322],[117.212396,39.770742]])