<style>
    * {

        --line-height-scaling: 1.2;
        
        --font-scaling: 80%;

        --font-size-h1: calc(2em * var(--font-scaling));    /* 32px scaled */
        --font-size-h2: calc(1.5em * var(--font-scaling));  /* 24px scaled */
        --font-size-h3: calc(1.17em * var(--font-scaling)); /* 18.72px scaled */
        --font-size-h4: calc(1em * var(--font-scaling));    /* 16px scaled */
        --font-size-h5: calc(0.83em * var(--font-scaling)); /* 13.28px scaled */
        --font-size-p: calc(1em * var(--font-scaling));     /* 16px scaled */

        --margin-title: 2rem;

        /* font-family: Times New Roman, sans-serif; */
        text-align: justify; /* Justifies the text */
    }

    .abstract {
        width: 80%;
        margin: 0 auto; /* Centers the div */
    }

    .abstract-title {
        text-align: center;
        font-weight: 900;
        font-size: 1.5rem
    }

    pre, code, code>span {
        font-family: 'JetBrains Mono', monospace; /* Set the font to JetBrains Mono */

    }


h1, h2, h3, h4, h5, p, li {
    line-height: calc(var(--line-height-scaling) * 1em);
}


    /* Ensure the title doesn't get numbered */
.title {
    counter-reset: none;  /* No numbering for title */
}

/* Initialize the counter after the first h1 (document title) */
h1:not(.title) {
    counter-reset: h2; /* Reset h2 counter when a new h1 starts */
    margin-left: 0;
    counter-increment: h1; /* Increment h1 counter */
}

h1:not(.title)::before {
    font-size: var(--font-size-h1);
    content: counter(h1, upper-roman) ". "; /* Roman numeral (I., II., ...) */
}

/* For H2: Decimal with h1 (e.g., I.1) */
h2 {
    font-size: var(--font-size-h2);
    counter-reset: h3; /* Reset h3 counter when a new h2 starts */
    margin-left: var(--margin-title);
}

h2::before {
    counter-increment: h2;
    content: counter(h1, upper-roman) "." counter(h2) " "; /* I.1 */
}

/* For H3: Lowercase letters (e.g., I.1.a) */
h3 {
    font-size: var(--font-size-h3);
    counter-reset: h4; /* Reset h4 counter when a new h3 starts */
    margin-left: var(--margin-title);
}

h3::before {
    counter-increment: h3;
    content: counter(h1, upper-roman) "." counter(h2) "." counter(h3, lower-alpha) " "; /* I.1.a */
}

h4 {
    font-size: var(--font-size-h4);
    margin-left: var(--margin-title);
}

h5 {
    font-size: var(--font-size-h5);
    margin-left: var(--margin-title);
}

p {
    font-size: var(--font-size-p);
}

.katex-display > .katex {
    justify-content: center;
    display: flex
}


</style>


<h1 style="text-align: center;" class="title">
    Advanced Quantum Optics <br>
    - <br>
    Study of a Single Quantum Emitter
    
</h1>

<p style="text-align: center;">
Léo BECHET, M2 CompuPhys 2024-2025
</p>

<div class="abstract">
<div class="abstract-title">Abstract</div>

This study investigates the photon emission dynamics of a single quantum emitter (dipole) in various structured environments: air, a perfect conductor, a gold bar, and two nano-antennas, using a commercial Finite-Difference Time-Domain (FDTD) simulation approach. We quantify enhancements in the total decay rate, radiative decay rate, absorption decay rate, and quantum yield across these configurations. While the dipole in air shows moderate enhancements, the perfect conductor significantly boosts total and radiative decay rates with substantial absorption losses. The gold bar leads to a high total decay rate but lower quantum yield due to non-radiative losses. In contrast, single and dual nano-antenna configurations optimize radiative emission efficiency and quantum yield, with the dual setup achieving minimal absorption losses. These findings underscore the crucial role of structured environments in enhancing the emission properties of quantum emitters and their potential in advancing photonic technologies.


</div>


<!-- <div id="TOC"></div> -->



# Introduction

Jean-Jacques Greffet's pioneering work on nanoantennas for light emission[1] has demonstrated how carefully engineered nanostructures can significantly enhance and control the emission properties of quantum emitters. By manipulating the local density of optical states, his research has enabled precise tuning of emission directionality, polarization, and intensity. Building on these principles, our work studies the dynamics of photon emission from a single quantum emitter positioned in various structured environments using FDTD simulations. 

We put in common our data with our fellow PICS students to ensure the accuracy and consistency of our results.


# Method

## Finite-Difference Time-Domain method

The Finite-Difference Time-Domain (FDTD) method is a powerful computational technique used to solve Maxwell's equations for electromagnetic wave propagation in complex environments. It discretizes both time and space, breaking down the simulation domain into a grid where the electric and magnetic field components are updated iteratively over time. This time-stepping approach captures the interaction between electromagnetic fields and materials with a high level of precision, making it suitable for modeling various optical phenomena, including light scattering, diffraction, and emission dynamics.

In the context of photon emission from a single quantum emitter, FDTD is particularly advantageous as it allows for the accurate modeling of how the dipole interacts with its surrounding environment, such as structured or nanostructured materials. The method can account for material properties, geometries, and even dispersive effects, enabling the quantification of changes in emission rates and the spatial distribution of emitted photons. This level of detail is crucial for understanding and optimizing light-matter interactions in photonic structures.


# Characterization of the Dipole

In this section, we characterize the dipole in air without any perturbing structures. The goal is to compute the power \( P_0 \) radiated by the dipole, the dipole moment amplitude, the possible phase differences between the dipole moment and the electric field at the dipole’s position, and the complex values of the dipole moment.

## Power Radiated by the Dipole (\( P_0 \))

To compute the power radiated by the dipole in air, we use the Poynting vector approach:

$$
\mathbf{S} = \frac{1}{2} \text{Re}(\mathbf{E} \times \mathbf{H}^*)
$$

where:
- \(\mathbf{E}\) and \(\mathbf{H}\) are the electric and magnetic field vectors, respectively,
- \(*\) denotes the complex conjugate.

We calculate the flux of the Poynting vector through a surface surrounding the dipole. The surface consists of six planes forming a cube. The flux through each surface is computed using the dot product of the Poynting vector with the surface normal vector. Summing the contributions from all six surfaces yields the total radiated power, \( P_0 \). The result is:

$$
P_0 = 0.00437 \text{ W}
$$

This value is then validated and corrected for units if necessary.

## Dipole Moment Amplitude

To compute the dipole moment amplitude (\( p \)) of the dipole, we use the following formula:

\[
p = \sqrt{\frac{12 \pi \epsilon_0 P_0}{\omega k^3}}
\]

where:
- \(\epsilon_0\) is the vacuum permittivity,
- \(P_0\) is the power radiated by the dipole,
- \(\omega = k c\) is the angular frequency of the dipole emission, with \( c \) as the speed of light,
- \( k = \frac{2\pi}{\lambda} \) is the wave number, with \( \lambda \) as the wavelength.

With the values plugged in, we obtain:

\[
p = 1.13 \times 10^{-24} \text{ C.m}
\]

This value represents the amplitude of the dipole moment.

## Phase Difference \( \phi \)

The phase difference \( \phi \) between the dipole moment and the electric field at the dipole position is computed using:

\[
\phi = \arcsin\left(\frac{2 P_0}{\omega p E_{\text{max}}}\right)
\]

where:
- \( P_0 \) is the radiated power,
- \( \omega \) is the angular frequency,
- \( p \) is the dipole moment amplitude,
- \( E_{\text{max}} \) is the maximum value of the electric field at the dipole position.

Solving this equation yields two possible values for \( \phi \):

\[
\phi_1 = 0.0004 \text{ rad}, \quad \phi_2 = \pi - \phi_1 = 3.1412 \text{ rad}
\]

These two values correspond to the two possible phase differences between the dipole moment and the electric field.

## Complex Dipole Moment

Using the computed amplitude and the two possible phase values, we calculate the two possible complex values of the dipole moment. The dipole moment is given by:

\[
\mathbf{p} = p e^{-i \phi} e^{i \theta}
\]

where:
- \( p \) is the amplitude,
- \( \phi \) is the phase difference,
- \( \theta \) is the angle of the electric field vector in the simulation (given as 89.9772°).

Substituting the values, the two complex dipole moments are:

\[
\mathbf{p}_1 = (9.01 \times 10^{-28}) + i (1.13 \times 10^{-24}) \, \text{C.m}
\]
\[
\mathbf{p}_2 = (2.28 \times 10^{-30}) - i (1.13 \times 10^{-24}) \, \text{C.m}
\]

These values represent the two possible complex dipole moments of the emitter when placed in air without perturbation.

# Other situations

## Perfect conductor

### Near a Perfect Conductor

In this section, we analyze the behavior of the dipole placed near a perfect conductor. We calculate the power radiated by the dipole, the total decay rate (\(\gamma_{\text{tot}}\)), the radiative decay rate (\(\gamma_{\text{rad}}\)), the absorption decay rate change, and the quantum yield of the system. The presence of the conductor significantly affects these quantities, offering insight into the interaction between the dipole and the nearby conductive surface.

#### Power Radiated by the Dipole Near a Perfect Conductor

We compute the power radiated (\(P\)) using the Poynting vector formulation, similar to the case in air but considering the fields' interaction with the perfect conductor. The power components along each axis are computed individually, and the total power is obtained by summing these components:

\[
P = P_{x+} + P_{x-} + P_{y+} + P_{y-} + P_{z+} + P_{z-}
\]

where \(P_{x+}\), \(P_{x-}\), \(P_{y+}\), \(P_{y-}\), \(P_{z+}\), and \(P_{z-}\) are the power contributions along each of the surface planes. Using two different dipole moments, \( p_1 \) and \( p_2 \), we calculate two possible values for the radiated power:

\[
P_1 = \frac{\omega}{2} \text{Im}(\bar{p}_1 \cdot E_{\text{max}})
\]
\[
P_2 = \frac{\omega}{2} \text{Im}(\bar{p}_2 \cdot E_{\text{max}})
\]

where:
- \( \omega \) is the angular frequency,
- \( \bar{p}_1 \) and \( \bar{p}_2 \) are the complex conjugates of the dipole moments,
- \( E_{\text{max}} \) is the maximum electric field value.

**Results:**
- \( P_1 \) yields a negative value of \(-0.000394 \, \text{W}\), indicating an issue or unphysical result.
- \( P_2 \) gives a positive value of \( 0.00867 \, \text{W} \), which is physically valid and retained for further calculations.

#### Total Decay Rate Enhancement (\(\gamma_{\text{tot}}\))

The total decay rate enhancement is calculated as:

\[
\gamma_{\text{tot}} = \frac{P_2}{P_0}
\]

where \(P_0\) is the power radiated by the dipole in air. Using the computed values:

\[
\gamma_{\text{tot}} = \frac{0.00867}{0.00437} = 1.9868
\]

This enhancement indicates that the presence of the perfect conductor nearly doubles the total decay rate compared to the free-space scenario.

#### Radiative Decay Rate Enhancement (\(\gamma_{\text{rad}}\))

The radiative decay rate enhancement is calculated by comparing the power \( P \) radiated in the presence of the conductor to the power radiated in air:

\[
\gamma_{\text{rad}} = \frac{P}{P_0} = \frac{0.00867}{0.00437} = 1.9815
\]

This value indicates a significant enhancement of the radiative component of the decay rate due to the presence of the perfect conductor.

#### Absorption Decay Rate Change (\(\gamma_{\text{loss}}\))

The absorption or non-radiative decay rate is computed as the difference between the total and radiative decay rates:

\[
\gamma_{\text{loss}} = \gamma_{\text{tot}} - \gamma_{\text{rad}} = 1.9868 - 1.9815 = 0.0053
\]

This small value indicates that most of the decay remains radiative even in the presence of the conductor.

#### Quantum Yield of the System

The quantum yield (\( Y \)) is the ratio of the radiative decay rate to the total decay rate:

\[
Y = \frac{\gamma_{\text{rad}}}{\gamma_{\text{tot}}} = \frac{1.9815}{1.9868} = 0.9947
\]

This high yield suggests that nearly all the energy emitted by the dipole is radiated, demonstrating that the system remains highly efficient even with the perfect conductor.

#### System Conclusions

The presence of a perfect conductor significantly enhances both the total and radiative decay rates of the dipole due to the formation of an image dipole within the conductor. The dipole’s oscillating charges induce a similar dipole inside the metal, with opposite phase, as like charges repel and opposite charges attract. This induced dipole mirrors the emitter’s oscillation, leading to constructive interference between the emitted and reflected fields. As a result, the electric field at the dipole’s location is amplified, effectively doubling the decay rates while keeping the absorption decay rate minimal. This strong coupling between the dipole and the conductor maintains a high quantum yield close to unity. Such behavior highlights the dipole-conductor interaction mechanism, which can be harnessed to enhance emission rates of quantum emitters and optimize photonic device performance.


### Near a Gold Bar

In this section, we examine the behavior of a dipole placed near a gold bar, following the same method used previously with the perfect conductor. We compute the total decay rate enhancement (\(\gamma_{\text{tot}}\)), the radiative decay rate enhancement (\(\gamma_{\text{rad}}\)), the absorption decay rate change (\(\gamma_{\text{loss}}\)), and the quantum yield of the system. The interaction between the dipole and the gold bar produces different results due to the material's properties.

**Results Summary:**

- **Total Decay Rate Enhancement (\(\gamma_{\text{tot}}\))**: The presence of the gold bar increases the total decay rate by a factor of approximately 4.73. This indicates a significant influence of the gold bar on the emitter, enhancing its overall decay processes.
- **Radiative Decay Rate Enhancement (\(\gamma_{\text{rad}}\))**: The radiative decay rate is enhanced by a factor of 2.998. While this is substantial, it is less than the total decay rate enhancement, suggesting the presence of non-radiative processes.
- **Absorption Decay Rate Change (\(\gamma_{\text{loss}}\))**: The non-radiative component increases significantly, with a value of 1.74. This indicates that energy losses due to absorption in the gold bar are significant when the dipole is placed nearby.
- **Quantum Yield**: The quantum yield drops to approximately 0.63, meaning that less than half of the emitted energy is radiative, with the rest being absorbed or dissipated as heat.

#### System Conclusions

The interaction of the dipole with the gold bar resembles that of the perfect conductor, as the dipole induces an image dipole within the metal. This process enhances the total and radiative decay rates through constructive interference between the emitted and reflected fields, similar to the mechanism observed with a perfect conductor. However, unlike a perfect conductor, gold is a real metal with intrinsic material losses. These losses, primarily due to plasmonic absorption and resistive heating, introduce non-radiative decay pathways that decrease the overall efficiency of light emission. Consequently, the quantum yield is lower compared to an ideal conductor because a portion of the dipole’s energy is dissipated as heat within the gold. This behavior highlights the trade-off inherent in using real-life metals, where optimizing the balance between radiative enhancement and minimizing absorption losses is essential for the efficient design of photonic devices and quantum emitter systems.


### Near a Single Nano-Antenna

In this section, we study the behavior of a dipole positioned near a single nano-antenna, using the same method as before to compute the enhancement of the total decay rate (\(\gamma_{\text{tot}}\)), the radiative decay rate (\(\gamma_{\text{rad}}\)), the absorption decay rate (\(\gamma_{\text{loss}}\)), and the quantum yield.

**Results Summary:**

- **Total Decay Rate Enhancement (\(\gamma_{\text{tot}}\))**: The nano-antenna significantly enhances the total decay rate by a factor of approximately 9.44. This high enhancement reflects the strong interaction between the dipole and the nano-antenna, which accelerates the decay processes.
- **Radiative Decay Rate Enhancement (\(\gamma_{\text{rad}}\))**: The radiative decay rate is enhanced by a factor of 7.97, indicating that the nano-antenna effectively channels a large portion of the energy into radiative emission.
- **Absorption Decay Rate Change (\(\gamma_{\text{loss}}\))**: The non-radiative losses are much smaller compared to the gold bar, with an absorption decay rate change of 1.47. This suggests that the nano-antenna introduces fewer losses and is more efficient at radiating energy.
- **Quantum Yield**: The system's quantum yield remains high at approximately 0.84, meaning that 84% of the emitted energy is radiative, with only 16% being lost to absorption.

#### System Conclusions

The presence of the single nano-antenna significantly enhances both the total and radiative decay rates of the dipole while keeping absorption losses relatively low. Unlike the gold bar, which introduces substantial non-radiative pathways due to its larger volume and associated material losses, the nano-antenna's compact and optimized design allows for efficient coupling with the dipole. This localized interaction enhances the radiative decay rate while minimizing the metal volume exposed to the electromagnetic field, reducing energy dissipation as heat. As a result, the nano-antenna achieves a higher quantum yield, demonstrating its effectiveness in enhancing light emission while minimizing absorption losses. This highlights the advantage of using nano-antennas to optimize the radiative properties of dipoles in photonic devices.



### Dipole Characterization Near Two Nano-Antennas

In this section, we analyze the behavior of a dipole placed near two nano-antennas using the same method as previously described. We calculate the enhancement of the total decay rate (\(\gamma_{\text{tot}}\)), the radiative decay rate (\(\gamma_{\text{rad}}\)), the absorption decay rate change (\(\gamma_{\text{loss}}\)), and the quantum yield.

**Results Summary:**

- **Total Decay Rate Enhancement (\(\gamma_{\text{tot}}\))**: With the dipole placed between two nano-antennas, the total decay rate increases significantly, reaching an enhancement factor of approximately 59.27. This large value suggests a strong coupling between the dipole and the nano-antenna system, leading to accelerated decay processes.
- **Radiative Decay Rate Enhancement (\(\gamma_{\text{rad}}\))**: The radiative decay rate sees a substantial enhancement, with a value of 53.84. This indicates that the two nano-antennas are highly efficient at directing the dipole’s energy into radiation.
- **Absorption Decay Rate Change (\(\gamma_{\text{loss}}\))**: The non-radiative loss remains modest compared to the radiative component, with a value of 5.42. This shows that the two nano-antenna configuration minimizes energy losses while enhancing emission.
- **Quantum Yield**: The quantum yield is high, at approximately 0.91, implying that over 90% of the emitted energy is radiative, with minimal absorption loss.

#### System Conclusions

The configuration of two nano-antennas demonstrates a superior ability to enhance the emission properties of the dipole, resulting in a higher quantum yield compared to a single nano-antenna. In the single antenna setup, only one side of the oscillating dipole effectively couples with the antenna, limiting the interaction and reducing overall efficiency. However, the dual-antenna setup leverages both sides of the dipole’s oscillation, boosting the coupling efficiency and enhancing the radiative decay rate significantly.

This symmetric interaction not only maximizes the dipole’s emission in multiple directions but also minimizes regions of energy dissipation as heat, thereby reducing non-radiative losses. The two-antenna configuration achieves an optimized balance between radiative enhancement and minimal absorption losses, resulting in a higher quantum yield. This highlights its effectiveness for applications in advanced photonic devices requiring efficient and controlled light emission.



# Conclusion

Through our investigations of a single quantum emitter (dipole) in various structured environments, we observed significant variations in photon emission dynamics across four configurations: air, a perfect conductor, a gold bar, and two nano-antennas. In air, the dipole exhibited a modest total decay rate enhancement, while the perfect conductor dramatically increased both the total decay and radiative decay rates, albeit with substantial absorption losses. The gold bar configuration showed a high total decay rate with significant non-radiative losses, resulting in a lower quantum yield. In contrast, the single nano-antenna significantly enhanced the radiative decay rate while maintaining a high quantum yield. The configuration with two nano-antennas further optimized the system, yielding exceptional enhancement in both total and radiative decay rates, coupled with minimal absorption losses and a high quantum yield. These findings underscore the critical role of structured environments in modulating the emission characteristics of quantum emitters, highlighting the potential of nano-antennas in advanced photonic applications.


# References 

<style>
.reference {
    font-family: 'Georgia', serif;
    line-height: 1.4;
    margin: 10px 0;
    padding: 5px;
}

.reference-author {
    font-weight: bold;
}

.reference-title {
    font-style: italic;
}



.reference-doi a {
    text-decoration: none;
}

.reference-doi a:hover {
    text-decoration: underline;
}
</style>

<div class="reference">
    [1]
    <span class="reference-author">Jean-Jacques Greffet.</span>
    <span class="reference-title">Nanoantennas for light emission.</span>
    <span class="reference-journal">Science</span>, 
    <span class="reference-year">2005</span>, 
    <span>308 N° 5728, pp. 1561 - 1563.</span>
    <span class="reference-doi">
        ⟨<a href="https://doi.org/10.1126/science.1113355" target="_blank">10.1126/science.1113355</a>⟩.
    </span> 
    ⟨hal-00116880⟩
</div>