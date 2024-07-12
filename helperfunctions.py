from dune.iga import ControlPoint, ControlPointNet, NurbsPatchData, IGAGrid

from dune.common.hashit import hashIt
from dune.iga.basis import preBasisTypeName
from dune.generator.generator import SimpleGenerator
from dune.iga.basis import defaultGlobalBasis
import dune.grid
import numpy as np
import matplotlib.pyplot as plt


def globalBasis(gv, tree):
    generator = SimpleGenerator("BasisHandler", "Ikarus::Python")

    pbfName = preBasisTypeName(tree, gv.cppTypeName)
    element_type = f"Ikarus::BasisHandler<{pbfName}>"
    includes = []
    includes += list(gv.cppIncludes)
    includes += ["dune/iga/nurbsbasis.hh"]
    includes += ["ikarus/python/basis/basis.hh"]

    moduleName = "Basis_" + hashIt(element_type)
    module = generator.load(
        includes=includes, typeName=element_type, moduleName=moduleName
    )
    basis = defaultGlobalBasis(gv, tree)
    return module.BasisHandler(basis)


def cantileverBeam(L, h, ref):
    cp1 = ControlPoint((0, 0, 0), 1)
    cp2 = ControlPoint((0, h, 0), 1)
    cp3 = ControlPoint((L, 0, 0), 1)
    cp4 = ControlPoint((L, h, 0), 1)

    netC = ((cp1, cp2), (cp3, cp4))
    net = ControlPointNet(netC)

    nurbsPatchData1 = NurbsPatchData(((0, 0, 1, 1), (0, 0, 1, 1)), net, (1, 1))
    nurbsPatchData2 = nurbsPatchData1.degreeElevate(0, 1)
    nurbsPatchDataFinal = nurbsPatchData2.degreeElevate(1, 1)

    grid = IGAGrid(nurbsPatchDataFinal)

    grid.grid.globalRefineInDirection(0, ref)
    return grid


def cube(L, ref):
    lowerLeft = []
    upperRight = []
    elements = []
    for i in range(3):
        lowerLeft.append(-L)
        upperRight.append(L)
        elements.append(ref)

    grid = dune.grid.structuredGrid(lowerLeft, upperRight, elements)
    return grid


# reference solution from Sze et al. 2004 (Table 2a)
def cantileverBeamRef(P0, Pmax):
    lfs = np.arange(0.05, 1.04, 0.05) * Pmax / P0  # load factors
    u = np.array(
        [
            0.026,
            0.103,
            0.224,
            0.381,
            0.563,
            0.763,
            0.971,
            1.184,
            1.396,
            1.604,
            1.807,
            2.002,
            2.19,
            2.37,
            2.541,
            2.705,
            2.861,
            3.01,
            3.151,
            3.286,
        ]
    )  # absolute value of horizontal displacement (x-direction)
    w = np.array(
        [
            0.663,
            1.309,
            1.922,
            2.493,
            3.015,
            3.488,
            3.912,
            4.292,
            4.631,
            4.933,
            5.202,
            5.444,
            5.660,
            5.855,
            6.031,
            6.190,
            6.335,
            6.467,
            6.588,
            6.698,
        ]
    )  # absolute value of vertical displacement (z-direction)
    return lfs, u, w


def loadDisplacement(lfref, uref, wref, lf, ufe, wfe):
    plt.plot(uref, lfref, color="black", label="u_ref", linewidth=3, marker="D")
    plt.plot(wref, lfref, color="black", label="w_ref", linewidth=3, marker="o")
    plt.plot(ufe, lf, color="red", label="u_FE", linewidth=3)
    plt.plot(wfe, lf, color="blue", label="w_FE", linewidth=3)
    plt.xlabel("u, w", fontsize=16)
    plt.ylabel("lambda", fontsize=16)
    plt.rc("xtick", labelsize=14)  # Set the font size for x tick labels
    plt.rc("ytick", labelsize=14)  # Set the font size for y tick labels
    plt.rc("legend", fontsize=14)  # Set the legend font size
    plt.rc("figure", titlesize=16)  # Set the font size of the figure title
    plt.legend(loc="lower right")
    plt.grid(True, which="both", ls="-", color="0.85")
    plt.tight_layout()
    plt.show()
    plt.close()
