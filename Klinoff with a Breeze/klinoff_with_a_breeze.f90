module constants
    implicit none
    real, parameter :: pi = 3.141592653589793
    real, parameter :: earth_radius = 6371.0 ! in kilometers
    real, parameter :: gravity = 9.81 ! in m/s^2
    real, parameter :: gas_constant = 287.05 ! in J/(kg*K)
    real, parameter :: lapse_rate = 0.0065 ! in K/m
    real, parameter :: sea_level_temp = 288.15 ! in K
    real, parameter :: sea_level_pressure = 101325.0 ! in Pa
end module constants

module weather_types
    implicit none
    type :: WeatherData
        real :: temperature
        real :: pressure
        real :: humidity
        real :: wind_speed
        real :: wind_direction
    end type WeatherData
end module weather_types

module weather_utils
    use constants
    implicit none
contains
    function calculate_pressure(altitude) result(pressure)
        real, intent(in) :: altitude
        real :: pressure
        pressure = sea_level_pressure * (1.0 - lapse_rate * altitude / sea_level_temp) ** (gravity / (gas_constant * lapse_rate))
    end function calculate_pressure

    function calculate_temperature(altitude) result(temperature)
        real, intent(in) :: altitude
        real :: temperature
        temperature = sea_level_temp - lapse_rate * altitude
    end function calculate_temperature

    function calculate_humidity(temp, pressure) result(humidity)
        real, intent(in) :: temp, pressure
        real :: humidity
        humidity = 0.5 * exp(-0.1 * (temp - 273.15)) * (pressure / sea_level_pressure)
    end function calculate_humidity

    subroutine print_weather_data(data)
        use weather_types
        implicit none
        type(WeatherData), intent(in) :: data
        write(*, '(A,F8.2,A)', advance='no') "Temperature: ", data%temperature, " K, "
        write(*, '(A,F10.2,A)', advance='no') "Pressure: ", data%pressure, " Pa, "
        write(*, '(A,F6.2,A)', advance='no') "Humidity: ", data%humidity, " %, "
        write(*, '(A,F6.2,A)', advance='no') "Wind Speed: ", data%wind_speed, " m/s, "
        write(*, '(A,F8.2,A)', advance='no') "Wind Direction: ", data%wind_direction, " degrees", char(13)
        call flush(6)
    end subroutine print_weather_data

    subroutine print_breeze_data(data, unit)
        use weather_types
        implicit none
        type(WeatherData), intent(in) :: data
        integer, intent(in) :: unit
        write(unit, '(A,F8.2,A)') "Wind Speed: ", data%wind_speed, " m/s"
        write(unit, '(A,F8.2,A)') "Wind Direction: ", data%wind_direction, " degrees"
        write(unit, *) "-----------------------------------"
        write(unit, *) ""
    end subroutine print_breeze_data
end module weather_utils

module config
    implicit none
    real :: initial_wind_speed = 5.0
    real :: initial_wind_direction = 90.0
    integer :: altitude_step = 1000
    integer :: max_altitude = 10000
end module config

program weather_simulation
    use constants
    use weather_types
    use weather_utils
    use config
    implicit none

    type(WeatherData) :: current_weather
    real :: altitude
    integer :: i
    character(len=1) :: choice
    character(len=100) :: filename
    integer :: unit

    call welcome_message()
    call fake_initializing_messages()
    call get_user_input()

    ! Initialize weather data
    current_weather%wind_speed = initial_wind_speed
    current_weather%wind_direction = initial_wind_direction

    ! Open file to save breeze data
    filename = 'breeze_data.txt'
    open(unit=10, file=filename, status='replace')

    ! Simulate weather for different altitudes
    do i = 0, max_altitude, altitude_step
        altitude = real(i)
        current_weather%temperature = calculate_temperature(altitude)
        current_weather%pressure = calculate_pressure(altitude)
        current_weather%humidity = calculate_humidity(current_weather%temperature, current_weather%pressure)
        write(*, '(A,F8.2,A)', advance='no') "Weather at altitude: ", altitude, " meters, "
        call print_weather_data(current_weather)
        write(10, '(A,F8.2,A)') "Altitude: ", altitude, " meters"
        call print_breeze_data(current_weather, 10)
        call precise_sleep(0.1, 0.7) ! Pause for a random time between 0.1 and 0.7 seconds
    end do
    close(10)
    print *, "Simulation complete! Breeze data saved to ", filename

contains

    subroutine welcome_message()
        print *, "==========================================================="
        print *, "  Welcome to the Klinoff with a Breeze Weather Simulation"
        print *, "==========================================================="
        call sleep(2)
    end subroutine welcome_message

    subroutine fake_initializing_messages()
        integer :: i
        character(len=3), dimension(3) :: dots = (/'.  ', '.. ', '...'/)
        do i = 1, 9
            write(*, '(A)', advance='no') "Initializing" // dots(mod(i-1, 3) + 1)
            call flush(6)
            call precise_sleep(0.1, 0.5)
            write(*, '(A)', advance='no') char(13) // "               " // char(13)
        end do
        print *, "Initialization complete!"
    end subroutine fake_initializing_messages

    subroutine get_user_input()
        print *, "Enter initial wind speed (m/s):"
        read *, initial_wind_speed
        print *, "Enter initial wind direction (degrees):"
        read *, initial_wind_direction
        print *, "Enter altitude step (meters):"
        read *, altitude_step
        print *, "Enter maximum altitude (meters):"
        read *, max_altitude
    end subroutine get_user_input

    subroutine sleep(seconds)
        integer, intent(in) :: seconds
        integer :: i
        do i = 1, seconds
            call system("ping -n 2 127.0.0.1 > nul")
        end do
    end subroutine sleep

    subroutine precise_sleep(min_seconds, max_seconds)
        real, intent(in) :: min_seconds, max_seconds
        real :: sleep_time, elapsed_time
        integer :: start_time, end_time, count_rate
        call random_number(sleep_time)
        sleep_time = min_seconds + sleep_time * (max_seconds - min_seconds)
        call system_clock(start_time, count_rate)
        elapsed_time = 0.0
        do while (elapsed_time < sleep_time)
            call system_clock(end_time)
            elapsed_time = real(end_time - start_time) / real(count_rate)
        end do
    end subroutine precise_sleep

end program weather_simulation