'''Particle Velocity

You are a programmer in a scientific team doing research into particles. As an experiment, you have measured
the position of a single particle in N equally distributed moments of time. The measurement made in moment K is
recorded in an array particles as particles[K].

Now, your job is to count all the periods of time when the movement of the particle was stable. Those are the
periods during which the particle doesn't change its velocity: i.e. the difference between any two consecutive
position measurements remains the same. Note that you need at least three measurements to be sure that the
particle didn't change its velocity.

For Example
1, 3, 5, 7, 9 is stable (velocity is 2)
7, 7, 7, 7 is stable (particle stays in place)
3, -1, -5, -9 is stable (velocity is 4)
0, 1 is not stable (you need at least three measurements)
1, 1, 2, 5, 7 is not stable (velocity changes between measurements)
More formally, your task is to find all the periods of time particles[P], particles[P+1], ....particles[Q]
(of length at least 3) during which the movement of the particle is stable. Note that some periods of time might
be contained in others (see below example).

Example:
Input: [-1, 1, 3, 3, 3, 2, 3, 2, 1, 0]
Output: 5'''


def particleVelocity(particles):

    if len(particles) < 3:
        return 0

    stableParticle = 0
    for i in range(len(particles) - 2):
        for j in range(i + 1, len(particles) - 1):
            if particles[j + 1] - particles[j] == particles[i + 1] - particles[i]:
                stableParticle += 1
            else:
                break
    return -1 if stableParticle > 10 ** 9 else stableParticle