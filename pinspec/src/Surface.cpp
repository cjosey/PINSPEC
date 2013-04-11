#include "Surface.h"

/**
 * @brief Surface class constructor.
 * @details By default, the constructor sets the surface boundary conditions
 *          to vacuum.
 */
Surface::Surface() {
    _boundary_type = VACUUM;
}


/**
 * @brief Surface destructor.
 */
Surface::~Surface() { }


/**
 * @brief Returns this Surface's boundary type.
 * @details Returns the Surface's boundary type which can be REFLECTIVE, VACUUM, 
 *          or INTERFACE.
 * @return Surface boundary type
 */
boundaryType Surface::getBoundaryType() const {
    return _boundary_type;
}


/**
 * @brief Sets the boundary type for this Surface. 
 * @details Sets the Surface's boundary type which can be REFLECTIVE, VACUUM, 
 *          or INTERFACE).
 * @param type the boundary type
 */
void Surface::setBoundaryType(boundaryType type) {
    _boundary_type = type;
}


/******************************************************************************
 *****************************   XPlane   *************************************
 *****************************************************************************/

/**
 * @brief The XPlane constructor.
 * @details Assigns a default value of x=0 for the x-axis intersection point.
 */
XPlane::XPlane() {
    _x = 0.0;
};


/**
 * @brief XPlane destructor.
 */
XPlane::~XPlane() { };


/**
 * @brief Returns the x-coordinate of the plane's intersection point with the 
 *        x-axis.
 * @return the x-coordinate of the intersection point
 */
float XPlane::getX() {
    return _x;
}


/**
 * @brief Sets the x-coordinate of the plane's intersection point with the 
 *        x-axis.
 * @param x the x-coordinate of the intersectiont point
 */
void XPlane::setX(float x) {
    _x = x;
}


/**
 * @brief Computes the nearest distance to the XPlane along a neutron's 
 *        trajectory.
 * @param neutron a pointer to a Neutron struct
 */
float XPlane::computeNearestDistance(neutron* neutron) {

    /* Set dist to infinity to begin with */
    float dist = std::numeric_limits<float>::infinity();
    float x = neutron->_x;
    float u = neutron->_u;

    if ((x < _x && u > 0.0) || (x > _x && u < 0.0))
        dist = (_x - x) / u;

    return dist;
}


/**
 * @brief Checks whether a neutron is on the XPlane.
 * @details The threshold used to compute whether or not a neutron is on the
 *          on the XPlane is 1E-6 for the difference between the x-coordinate 
 *          of the neutron's position and the location of the XPlane.
 * @param neutron the neutron of interest
 * @return true if on the XPlane, otherwise false
 */
bool XPlane::onSurface(neutron* neutron) {
    if (fabs(_x - neutron->_x) < 1E-6)
        return true;

    return false;
}



/******************************************************************************
 *****************************   YPlane   *************************************
 *****************************************************************************/

/**
 * @brief The YPlane constructor.
 * @details Assigns a default value of y=0 for the y-axis intersection point.
 */
YPlane::YPlane() {
    _y = 0.0;
};


/**
 * @brief YPlane destructor.
 */
YPlane::~YPlane() { };



/**
 * @brief Returns the y-coordinate of the plane's intersection point with the 
 *        y-axis.
 * @return the y-coordinate of the intersection point
 */
float YPlane::getY() {
    return _y;
}


/**
 * @brief Sets the x-coordinate of the plane's intersection point with the 
 *        y-axis.
 * @param y the y-coordinate of the intersectiont point
 */
void YPlane::setY(float y) {
    _y = y;
}


/**
 * @brief Computes the nearest distance to the YPlane along a neutron's 
 *        trajectory.
 * @param neutron a pointer to a Neutron struct
 */
float YPlane::computeNearestDistance(neutron* neutron) {

    /* Set dist to infinity to begin with */
    float dist = std::numeric_limits<float>::infinity();
    float y = neutron->_y;
    float v = neutron->_v;

    if ((y < _y && v > 0.0) || (y > _y && v < 0.0))
        dist = (_y - y) / v;

    return dist;
}


/**
 * @brief Checks whether a neutron is on the YPlane.
 * @details The threshold used to compute whether or not a neutron is on the
 *          on the YPlane is 1E-6 for the difference between the y-coordinate 
 *          of the neutron's position and the location of the YPlane
 * @param neutron the neutron of interest to check
 * @return true if on the YPlane, otherwise false
 */
bool YPlane::onSurface(neutron* neutron) {
    if (fabs(_y - neutron->_y) < 1E-6)
        return true;

    return false;
}



/******************************************************************************
 *****************************   Circle   *************************************
 *****************************************************************************/

/**
 * @brief The Circle constructor.
 * @details Assigns default values for the center of the circle (x=0, y=0)
 *          and a radius of 0.
 */
Circle::Circle() {
    _x0 = 0;
    _y0 = 0;
    _r = 0;
    _r_squared = 0;
};


/**
 * @brief Circle destructor.
 */
Circle::~Circle() { };


/**
 * @brief Returns the x-coordinate of the circle's center.
 * @return the x-coordinate of the circle center
 */
float Circle::getX0() {
    return _x0;
}


/**
 * @brief Returns the y-coordinate of the circle's center.
 * @return the y-coordinate of the circle center
 */
float Circle::getY0() {
    return _y0;
}


/**
 * @brief Returns the radius of the circle.
 * @return the circle radius
 */
float Circle::getRadius() {
    return _r;
}


/**
 * @brief Sets the x-coordinate of the circle's center.
 * @param x0 the x-coordinate of the circle center
 */
void Circle::setX0(float x0) {
     _x0 = x0;
}


/**
 * @brief Sets the y-coordinate of the circle's center.
 * @param y0 the y-coordinate of the circle center
 */
void Circle::setY0(float y0) {
    _y0 = y0;
}


/**
 * @brief Sets the radius of the circle's center.
 * @param r the circle's radius
 */
void Circle::setRadius(float r) {
     _r = r;
     _r_squared = r*r;
}


/**
 * @brief Computes the nearest distance to the Circle along a neutron's 
 *        trajectory.
 * @param neutron a pointer to a Neutron struct
 */
float Circle::computeNearestDistance(neutron* neutron) {

    float x = neutron->_x;
    float y = neutron->_y;
    float u = neutron->_u;
    float v = neutron->_v;

    /* Compute temporary variables for each term in the quadratic equation */
    float a = u*u + v*v;
    float b = 2.0*x*u - 2.0*_x0*u + 2.0*y*v - 2.0*_y0*v;
    float c = x*x + _x0*_x0 - 2.0*_x0*x + y*y + _y0*_y0 - 2.0*_y0*y 
                  - _r_squared;

    /* Compute the discriminant in the quadratic formula */
    float discr = b*b - 4.0*a*c;

    /* There is not an intersection point */
    if (discr < 0.0)
        return std::numeric_limits<float>::infinity();

    /* There is one intersection point */
    else if (discr == 0.0) {

        float dist = -b / (2.0*a);

    if (dist >= 0.0)
        return dist;
    else
        return std::numeric_limits<float>::infinity();
    }

    /* There are two intersection points */
    else {
    discr = sqrt(discr);
    float dist1 = (-b + discr) / (2.0*a);
    float dist2 = (-b - discr) / (2.0*a);

    if (dist1 <= dist1 && dist1 > 0.0)
        return dist1;
    else if (dist2 <= dist1 && dist2 > 0.0)
        return dist2;
    else
        return std::numeric_limits<float>::infinity();
    }
}


/**
 * @brief Checks whether a neutron is on the Circle.
 * @details The threshold used to compute whether or not a neutron is on the
 *          on the neutron is 1E-6 for the difference between the distance
 *          between the neutron and the circle center and the radius of the
 *          circle.
 * @param neutron the neutron of interest
 * @return true if on the XPlane, otherwise false
 */
bool Circle::onSurface(neutron* neutron) {

    float r_squared = (neutron->_y - _y0) * (neutron->_y - _y0) + 
                       (neutron->_x - _x0) * (neutron->_x - _x0);

    if (fabs(_r_squared - r_squared) < 1E-6)
        return true;
    else
        return false;
}