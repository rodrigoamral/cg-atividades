import numpy as np
import pytest
from src.leitorObj import OBJModelLoader

def test_get_faces_before_loading():
    obj_loader = OBJModelLoader("triangulo.obj")  
    faces = obj_loader.get_faces()
    assert faces is None


def test_get_faces_with_missing_file():
    obj_loader = OBJModelLoader("triangulo.obj")  
    faces = obj_loader.get_faces()
    assert faces is None

def test_get_vertices():
    obj_loader = OBJModelLoader("triangulo.obj")  
    vertices = obj_loader.get_vertices()
    expected_vertices = np.array([[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.5, 1.0, 0.0]])  
    assert np.array_equal(vertices, expected_vertices)

def test_get_faces():
    obj_loader = OBJModelLoader("triangulo.obj") 
    faces = obj_loader.get_faces()
    expected_faces = np.array([[1, 2, 3]])  
    assert np.array_equal(faces, expected_faces)


