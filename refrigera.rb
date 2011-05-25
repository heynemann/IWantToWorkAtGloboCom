class Refrigerator
  attr_reader :total_cost, :temp

  def initialize(temp, step)
    @temp = temp
    @step = step
  end

  def tick
    @temp += @step
  end

  def reduz_um_grau
    @total_cost.nil? ? @total_cost = 0.5 : @total_cost += 0.1
    @temp -= 1
  end
end

module Refrigera
  module_function

  def refrigera(initial_temp, wanted_temp, options = {})
    duration = options[:duration] ||= 360
    step = options[:step] ||= 0.5
    variation = options[:variation] ||= 2

    initial_temp = initial_temp.to_f
    wanted_temp = wanted_temp.to_f

    min_temp = wanted_temp - variation
    max_temp = wanted_temp + variation
    ref = Refrigerator.new(initial_temp, step)

    duration.times do |i|
      if ref.temp >= max_temp
        time_left = duration - i
        [time_left * step, ref.temp - min_temp].min.ceil.times { ref.reduz_um_grau }
      end
      raise "I'm freezing!!! #{ref.temp}" if ref.temp < min_temp
      ref.tick
      raise "Hell it's HOT!!! #{ref.temp}" if ref.temp > max_temp
    end
    puts ref.total_cost
  end
end

Refrigera.refrigera(30, 20)
