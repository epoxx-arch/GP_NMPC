def gt():
    mass = 1.98
    lf = 0.125
    lr = 0.125
    Iz = 0.024
    Df = 0.8 * mass * 9.81 / 2.0
    Cf = 1.25 # 1.25
    Bf = 1.0
    Dr = 0.8 * mass * 9.81 / 2.0
    Cr = 1.25 # 1.25
    Br = 1.0

    Cm1 = mass
    Cm2 = 0
    Cr0 = 0
    Cr2 = 0

    max_acc = 10.  # max acceleration [m/s^2]
    min_acc = -10.  # max deceleration [m/s^2]
    max_steer = 0.5  # max steering angle [rad]
    min_steer = -0.5  # min steering angle [rad]
    max_steer_vel = 5.  # max steering velocity [rad/s]


    max_inputs = [max_acc, max_steer]
    min_inputs = [min_acc, min_steer]

    max_rates = [None, max_steer_vel]
    min_rates = [None, -max_steer_vel]

    params = {
        'lf': lf,
        'lr': lr,
        'mass': mass,
        'Iz': Iz,
        'Bf': Bf,
        'Br': Br,
        'Cf': Cf,
        'Cr': Cr,
        'Df': Df,
        'Dr': Dr,
        'Cm1': Cm1,
        'Cm2': Cm2,
        'Cr0': Cr0,
        'Cr2': Cr2,
        'max_acc': max_acc,
        'min_acc': min_acc,
        'max_steer': max_steer,
        'min_steer': min_steer,
        'max_steer_vel': max_steer_vel,
        'max_inputs': max_inputs,
        'min_inputs': min_inputs,
        'max_rates': max_rates,
        'min_rates': min_rates,
    }
    return params


def errordy():
    mass = 1.98
    lf = 0.125
    lr = 0.125
    Iz = 0.024
    Df = 0.8 * mass * 9.81 / 2.0
    Cf = 1.25
    Bf = 1.0
    Dr = 0.8 * mass * 9.81 / 2.0
    Cr = 1.25
    Br = 1.0

    Cm1 = mass
    Cm2 = 0
    Cr0 = 0
    Cr2 = 0

    max_acc = 10.  # max acceleration [m/s^2]
    min_acc = -10.  # max deceleration [m/s^2]
    max_steer = 0.5  # max steering angle [rad]
    min_steer = -0.5  # min steering angle [rad]
    max_steer_vel = 5.  # max steering velocity [rad/s]


    max_inputs = [max_acc, max_steer]
    min_inputs = [min_acc, min_steer]
    max_rates = [None, max_steer_vel]
    min_rates = [None, -max_steer_vel]

    params1 = {
        'lf': lf,
        'lr': lr,
        'mass': mass,
        'Iz': Iz,
        'Bf': Bf,
        'Br': Br,
        'Cf': Cf,
        'Cr': Cr,
        'Df': Df,
        'Dr': Dr,
        'Cm1': Cm1,
        'Cm2': Cm2,
        'Cr0': Cr0,
        'Cr2': Cr2,
        'max_acc': max_acc,
        'min_acc': min_acc,
        'max_steer': max_steer,
        'min_steer': min_steer,
        'max_steer_vel': max_steer_vel,
        'max_inputs': max_inputs,
        'min_inputs': min_inputs,
        'max_rates': max_rates,
        'min_rates': min_rates,
    }
    return params1