"""
date: Tue Sep 16 10:20:15 2025
author: rfetick
"""

import os
import numpy as np
import oao25


def load_data(name):
    """Load data from the <oao25/data/> folder"""
    path = os.path.dirname(oao25.__file__) + os.path.sep + 'data' + os.path.sep
    return np.load(path + name)


def compute_cog(img, bkg, integer=False, low=0.1):
    """
    Compute the center of gravity of an image.
    Threshold pixels lower than `low*np.max(img)`
    """
    x = np.arange(0,img.shape[1])
    y = np.arange(0,img.shape[0])
    X,Y = np.meshgrid(x,y)
    img_filtered = (img - bkg) - np.median(img - bkg)
    img_filtered = np.clip(img_filtered - low*np.max(img_filtered), 0, None)
    cx = np.sum(img_filtered*X)/np.sum(img_filtered)
    cy = np.sum(img_filtered*Y)/np.sum(img_filtered)
    if integer:
        cx = int(np.round(cx))
        cy = int(np.round(cy))
    return cx, cy


def center_cog(img, bkg, nx):
    """Center an image on its CoG"""
    cx,cy = compute_cog(img, bkg, integer=True)
    m_center = img[cy-nx//2:cy+nx//2,cx-nx//2:cx+nx//2]
    bkg_center = bkg[cy-nx//2:cy+nx//2,cx-nx//2:cx+nx//2]
    return m_center, bkg_center
